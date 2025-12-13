# Django Social Media API

A simple Django REST API for user registration, authentication, and profile management. Built with Django and Django REST Framework (DRF).

## Features

- Custom user model extending Django's `AbstractUser`
  - Additional fields: `bio`, `profile_picture`, `followers` (ManyToMany)
- User registration
- Token-based authentication
- User profile retrieval
- API endpoints structured under `/accounts/`

Endpoints:

Endpoint	Method	Description
/api/posts/	GET	List all posts
/api/posts/	POST	Create a new post
/api/posts/<id>/	GET	Retrieve a post
/api/posts/<id>/	PUT/PATCH	Update a post (owner only)
/api/posts/<id>/	DELETE	Delete a post (owner only)
/api/posts/<post_pk>/comments/	GET	List comments for a post
/api/posts/<post_pk>/comments/	POST	Create comment for a post

