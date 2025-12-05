Comments System
---------------

Overview:
- Users can add comments to posts.
- Only authenticated users may create comments.
- Only the author of a comment may edit or delete it.
- Comment timestamps: `created_at` (when created) and `updated_at` (last modified).

How to use:
- On a post detail page (e.g. /post/<post_id>/), scroll to the comments section.
- Logged-in users will see a comment box; enter text and click "Post Comment".
- Authors of comments will see "Edit" and "Delete" links beside their comment.

Admin/Developer notes:
- Comment model: `blog.Comment` (fields: post FK, author FK, content, created_at, updated_at).
- Migrations: run `python manage.py makemigrations blog` and `python manage.py migrate`.
- URLs:
    - Create:  post/<post_id>/comments/new/  -> `comment-create`
    - Edit:    comment/<pk>/edit/           -> `comment-update`
    - Delete:  comment/<pk>/delete/         -> `comment-delete`
- Views: create is function-based `add_comment`, edit/delete are class based (`CommentUpdateView`, `CommentDeleteView`).
- Templates:
    - `blog/_comments.html` included in `post_detail.html`
    - `blog/comment_form.html`
    - `blog/comment_confirm_delete.html`
