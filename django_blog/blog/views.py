from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from .models import Post
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


# Create your views here.


# List all posts
class PostListView(ListView):
    model = Post
    template_name = 'blog/posts.html'  # template to render
    context_object_name = 'posts'
    ordering = ['-id']  # latest first

# View a single post
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

# Create a new post
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'blog/post_form.html'
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# Update a post
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'blog/post_form.html'
    fields = ['title', 'content']

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

# Delete a post
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('posts')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


def home(request):
    return render(request, 'blog/home.html')


@login_required
def profile_view(request):
    if request.method == 'POST':
        # Updating user data
        user = request.user
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.email = request.POST.get('email')
        user.save()

        messages.success(request, "Profile updated successfully!")
        return redirect('profile')

    return render(request, 'blog/profile.html')


# Register view
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # log in automatically after registration
            return redirect('profile')  # redirect to profile page
    else:
        form = UserCreationForm()
    return render(request, 'blog/register.html', {'form': form})

# Login view
from django.contrib.auth.views import LoginView

class CustomLoginView(LoginView):
    template_name = 'blog/login.html'

# Profile view
@login_required
def profile_view(request):
    return render(request, 'blog/profile.html')



def posts_view(request):
    posts = Post.objects.all()
    return render(request, 'blog/posts.html', {'posts': posts})

# For dynamic title in template
PostCreateView.action = "Create"
PostUpdateView.action = "Edit"
