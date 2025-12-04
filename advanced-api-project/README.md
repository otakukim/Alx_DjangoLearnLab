# Book API — Django REST Framework

This API provides CRUD operations for a Book model using Django REST Framework's
generic class-based views and permission system.

## Endpoints

| Method | Endpoint                  | Description                     | Permission |
|--------|---------------------------|---------------------------------|------------|
| GET    | /books/                   | List all books                  | AllowAny   |
| GET    | /books/<id>/              | Retrieve single book            | AllowAny   |
| POST   | /books/create/            | Create new book                 | Auth only  |
| PUT    | /books/<id>/update/       | Update existing book            | Auth only  |
| DELETE | /books/<id>/delete/       | Delete a book                   | Auth only  |

## Customizations
- Validation added inside the serializer.
- `perform_create` and `perform_update` hooks used for custom actions.
- Permissions enforce read-only for public users and write-access for authenticated users.

## Testing
Use Postman, curl, or DRF's browsable API.
Test both authenticated and unauthenticated requests.
