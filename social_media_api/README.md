# Django Social Media API

A simple Django REST API for user registration, authentication, and profile management. Built with Django and Django REST Framework (DRF).

## Features

- Custom user model extending Django's `AbstractUser`
  - Additional fields: `bio`, `profile_picture`, `followers` (ManyToMany)
- User registration
- Token-based authentication
- User profile retrieval
- API endpoints structured under `/accounts/`

## Project Structure

