# README.md

## Introduction to Django Development Environment Setup

I installed Django and created a new Django project named LibraryProject. 
This initial setup will serve as the foundation for developing Django applications.

### Integrating Book Model with Django Admin Interface

#### Registering the Book Model
- The `Book` model was registered with the Django admin by modifying `bookshelf/admin.py` to include the `Book` model.

#### Customizing the Admin Interface
- The admin interface for the `Book` model was customized to display the `title`, `author`, and `publication_year` in the list view.
- Filters for `author` and `publication_year` were added to the sidebar for better navigation.
- A search bar was enabled to search for books by `title` or `author`.

#### Steps to Access the Admin Interface
1. Start the Django development server.
2. Navigate to `http://127.0.0.1:8000/admin/`.
3. Log in with the superuser credentials.
4. Manage `Book` entries through the admin interface.


### Custom Permissions and Groups

This project includes custom permissions for the MyModel model, which control who can view, create, edit, and delete instances of this model.

#### Permissions:
- `can_view`: Allows viewing of model instances.
- `can_create`: Allows creating new instances.
- `can_edit`: Allows editing existing instances.
- `can_delete`: Allows deletion of instances.

#### Groups:
- **Admins:** Have full permissions, including delete.
- **Librarians:** Can create and edit instances.
- **Members:** Can only view instances.

### Testing
- Test users have been created to verify that permissions are correctly enforced.
- Users in the Librarians group can create and edit but cannot delete.
- Users in the Members group can only view instances.