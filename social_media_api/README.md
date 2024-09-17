# Social Media API Project

This project is a simple social media API built using Django and Django REST Framework, with custom user authentication and token-based authentication for API requests.

## Table of Contents

1. [Project Setup](#project-setup)
2. [User Model Overview](#user-model-overview)
3. [Registering a User](#registering-a-user)
4. [Authenticating a User](#authenticating-a-user)
5. [Testing the API](#testing-the-api)

## Project Setup

Follow these steps to set up the project locally:

### 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/social_media_api.git
cd <your-repository>
```

### 2. Create a Virtual Environment

Create a virtual environment to isolate the project dependencies.

```bash
python -m venv .env
source .env/bin/activate  # On MacOS 
.env\Scripts\activate # On Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up the Database

Apply migrations to set up the database schema.

```bash
python manage.py migrate
```

### 5. Run the Development Server

Start the Django development server.

```bash
python manage.py runserver
Your local development server will be running at: `http://127.0.0.1:8000/`.
```

## 2. User Model Overview

The custom user model in this project extends Django's AbstractUser and includes the following additional fields:

`bio`: A text field to allow users to add a short biography.
`profile_picture`: An image field to allow users to upload a profile picture.
`followers`: A Many-to-Many field to track user followers, referencing the `User` model itself (with `symmetrical=False` to allow one-way following).

User model Example

```python
# social_media_api/accounts/models.py

from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    followers = models.ManyToManyField('self', symmetrical=False, related_name='following')
    
    def __str__(self):
        return self.username
```

## 3. Registering a User

To register a user, send a `POST` request to the `http://127.0.0.1:8000/api/accounts/register/` endpoint.

**Register Endpoint:**
`POST http://127.0.0.1:8000/api/accounts/register/`

**Request Body (JSON):**

```json
{
  "username": "newuser",
  "password": "newpassword",
  "bio": "This is the new user's bio"
}
```

**Response (Success):**

```json
{
  "status": "User created successfully",
  "token": "generated_token_here",
  "user": {
    "username": "newuser",
    "bio": "This is the new user's bio"
  }
}
```

The response will include a token that can be used for authentication in future API requests once the user is registered.

## 4. Authenticating a User

This API uses token-based authentication. After a user is registered, they receive a token that should be included in the header of every request that requires authentication.

**Login Endpoint:**
To retrieve an authentication token for a user, send a `POST` request to the `http://127.0.0.1:8000/api/accounts/login/` endpoint with valid credentials.

**Endpoint:**
`POST http://127.0.0.1:8000/api/accounts/login/`

**Request Body (JSON):**

```json
{
  "username": "newuser",
  "password": "newpassword",
}
```

**Response (Success):**

```json
{
  "token": "generated_token_here"
}
```

**Using the Token:**
For authenticated requests, include the token in the `Authorization` header as a Bearer token.

```bash
Authorization: Token generated_token_here
```

## 5. Testing the API

To test the registration and authentication flows, you can use tools like [Postman](https://www.postman.com/) or [Curl](https://curl.se/) or use the terminal on your OS.

**Registration with Curl Example:**

```bash
curl -X POST http://127.0.0.1:8000/api/accounts/register/ \
-H "Content-Type: application/json" \
-d '{"username": "newuser", "password": "newpassword", "bio": "This is the new user's bio"}'
```

**Login with Curl Example:**

```bash
curl -X POST http://127.0.0.1:8000/api/accounts/login/ \
-H "Content-Type: application/json" \
-d '{"username": "newtuser", "password": "newpassword"}'
```

Make sure to replace `newtuser` and `newpassword` with the actual user credentials during testing.

### Conclusion

This README provides all the necessary steps to set up the project, register and authenticate users, and interact with the API. For further details or contributions, feel free to create issues or submit pull requests on the repository.

**NOTE:**
Feel free to modify or expand this README as needed for your project!
