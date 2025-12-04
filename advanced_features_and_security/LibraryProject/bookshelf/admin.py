from django.contrib import admin

# Register your models here.

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('date_of_birth', 'profile_photo')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Additional Info', {'fields': ('date_of_birth', 'profile_photo')}),
    )
    list_display = ('username', 'email', 'is_staff', 'date_of_birth')


admin.site.register(CustomUser, CustomUserAdmin)
from django.contrib.auth.models import Group, Permission
from advanced_features_and_security.models import Book
from django.contrib.contenttypes.models import ContentType

# Get ContentType for Book
book_ct = ContentType.objects.get_for_model(Book)

# Get permissions
can_view = Permission.objects.get(codename="can_view", content_type=book_ct)
can_create = Permission.objects.get(codename="can_create", content_type=book_ct)
can_edit = Permission.objects.get(codename="can_edit", content_type=book_ct)
can_delete = Permission.objects.get(codename="can_delete", content_type=book_ct)

# Create groups
viewers = Group.objects.create(name="Viewers")
editors = Group.objects.create(name="Editors")
admins = Group.objects.create(name="Admins")

# Assign permissions
viewers.permissions.add(can_view)
editors.permissions.add(can_view, can_create, can_edit)
admins.permissions.add(can_view, can_create, can_edit, can_delete)

