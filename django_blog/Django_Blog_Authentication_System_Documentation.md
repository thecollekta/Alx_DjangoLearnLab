# Django Blog Authentication System Documentation

## Overview

This document provides a comprehensive guide to the authentication system implemented in the Django Blog project. The system includes user registration, login, logout, and profile management functionalities.

## Features

1. User Registration
2. User Login
3. User Logout
4. Profile Management

## Implementation Details

### 1. User Registration

#### View

The registration functionality is handled by a custom view in `blog/views.py`:

```python
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
```

#### Form

We use a custom form that extends Django's `UserCreationForm` to include an email field:

```python
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
```

#### Template

The registration template (`templates/registration/register.html`) extends the base template and includes the registration form.

### 2. User Login

We use Django's built-in `LoginView` for handling user login.

#### URL Configuration

In `blog/urls.py`:

```python
path('login/', auth_views.LoginView.as_view(), name='login'),
```

#### Template

The login template (`templates/registration/login.html`) extends the base template and includes the login form.

#### Settings

In `django_blog/settings.py`:

```python
LOGIN_REDIRECT_URL = 'home'
```

### 3. User Logout

We use Django's built-in `LogoutView` for handling user logout.

#### URL Configuration

In `blog/urls.py`:

```python
path('logout/', auth_views.LogoutView.as_view(), name='logout'),
```

#### Template

The logout link is included in the base template (`templates/blog/base.html`) as a form to ensure it sends a POST request:

```html
</head>
<body>
    <header>
        <nav>
            <ul>
                {% if user.is_authenticated %}
                    <li>
                        <form id="logout-form" action="{% url 'logout' %}" method="POST" style="display: none;">
                            {% csrf_token %}
                        </form>
                        <a href="#" onclick="event.preventDefault(); document.getElementById('logout-form').submit();">
                            Logout
                        </a>
```

#### Settings

In `django_blog/settings.py`:

```python
LOGOUT_REDIRECT_URL = 'login'
```

### 4. Profile Management

#### View

Profile management is handled by a custom view in `blog/views.py`:

```python
@login_required
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserProfileForm(instance=request.user)
    return render(request, 'registration/register.html', {'form': form})
```

#### Form

We use a custom form for profile management:

```python
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']
```

#### Template

The profile template (`templates/registration/profile.html`) extends the base template and includes the profile management form.

## URL Configuration

The complete URL configuration for the authentication system in `blog/urls.py`:

```python
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
]
```

## Testing the Authentication System

1. Registration:

   - Navigate to `/accounts/register/`
   - Fill out the form with a new username, email, and password
   - Submit the form and verify that you're redirected to the profile page
2. Login:

   - Navigate to `/accounts/login/`
   - Enter your username and password
   - Verify that you're redirected to the profile page after successful login
3. Logout:

   - Click the "Logout" button in the navigation menu
   - Verify that you're logged out and redirected to the login page
4. Profile Management:

   - Log in and navigate to `/accounts/profile/`
   - Update your username or email
   - Submit the form and verify that your changes are saved

## Security Considerations

1. CSRF protection is enabled for all POST requests.
2. Passwords are securely hashed using Django's built-in password hashing system.
3. The logout functionality uses a POST request to prevent CSRF attacks.
4. The `@login_required` decorator is used to protect the profile view from unauthorized access.

## Conclusion

This authentication system provides a solid foundation for user management in the Django blog project. It includes all the basic functionality for user registration, login, logout, and profile management while maintaining security best practices.
