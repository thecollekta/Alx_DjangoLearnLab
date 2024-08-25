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

#### Permissions

- `can_view`: Allows viewing of model instances.
- `can_create`: Allows creating new instances.
- `can_edit`: Allows editing existing instances.
- `can_delete`: Allows deletion of instances.

#### Groups

- **Admins:** Have full permissions, including delete.
- **Librarians:** Can create and edit instances.
- **Members:** Can only view instances.

### Testing

- Test users have been created to verify that permissions are correctly enforced.
- Users in the Librarians group can create and edit but cannot delete.
- Users in the Members group can only view instances.

## LibraryProject

## Overview

LibraryProject is a Django-based web application designed to manage a library's collection of books. This document outlines the security measures implemented to protect the application from common vulnerabilities.

## Security Measures

### 1. Debug Mode

- **Setting:** `DEBUG = False`
- **Reason:** Ensures that detailed error pages are not exposed to end-users in a production environment, preventing sensitive information leakage.

### 2. Browser-Side Security Protections

- **Settings:**
  - `SECURE_BROWSER_XSS_FILTER = True`
  - `X_FRAME_OPTIONS = 'DENY'`
  - `SECURE_CONTENT_TYPE_NOSNIFF = True`
- **Reason:** Protects against cross-site scripting (XSS) attacks, clickjacking, and content type sniffing by enforcing strict browser policies.

### 3. Secure Cookies

- **Settings:**
  - `CSRF_COOKIE_SECURE = True`
  - `SESSION_COOKIE_SECURE = True`
- **Reason:** Ensures that session and CSRF cookies are only transmitted over secure HTTPS connections, protecting them from being intercepted by attackers.

### 4. Cross-Site Request Forgery (CSRF) Protection

- **Implementation:** All forms include `{% csrf_token %}` to protect against CSRF attacks.
- **Reason:** CSRF tokens verify that form submissions are legitimate and originate from the authenticated user.

### 5. SQL Injection Prevention

- **Implementation:** All database queries are handled using Django’s ORM, avoiding raw SQL queries.
- **Reason:** Parameterized queries prevent attackers from injecting malicious SQL code.

### 6. Content Security Policy (CSP)

- **Implementation:** Configured using `django-csp` middleware to restrict the sources from which content can be loaded.
- **Reason:** Mitigates the risk of XSS attacks by specifying trusted content sources.

## Tests

### Security Testing Procedures

- **CSRF Protection Testing:**
  - Attempted to submit forms without the CSRF token and confirmed that requests were blocked.

- **XSS Protection Testing:**
  - Injected scripts into form fields and URL parameters to verify that they were not executed.

- **SQL Injection Testing:**
  - Tested search fields and other user inputs for SQL injection vulnerabilities using tools like sqlmap.

- **CSP Testing:**
  - Verified the Content Security Policy header using browser developer tools to ensure that only allowed sources were used for loading content.

### Conclusion

The security measures implemented in this project are designed to protect against common vulnerabilities such as XSS, CSRF, and SQL injection. Regular audits and updates to these measures are recommended to maintain a high level of security.

## License

This project is for practice only.
