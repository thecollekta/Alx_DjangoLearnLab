# Social Media API Project

This project is a simple social media API built using Django and Django REST Framework, with custom user authentication and token-based authentication for API requests.

## Table of Contents

1. [Project Setup](#project-setup)
2. [User Model Overview](#user-model-overview)
3. [Registering a User](#registering-a-user)
4. [Authenticating a User](#authenticating-a-user)
5. [Testing the API](#testing-the-api)
6. [Implementing Posts and Comments Functionality](#implementing-posts-and-comments-functionality)

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
  "username": "Festus",
  "password": "qazwsxedc.",
  "bio": "This is Festus's bio"
}
```

```json
{
  "username": "Aboagye",
  "password": "qazwsxedc.",
  "bio": "This is Aboagye's bio"
}
```

**Response (Success):**

```json
{
  "status": "User created successfully",
  "token": "86eb3d31a8579246b218e8b212fb2c1c18f91921",
  "user": {
      "username": "Festus",
      "bio": "This is Festus's bio"
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
  "username": "Festus",
  "password": "qazwsxedc."
}
```

```json
{
  "username": "Aboagye",
  "password": "qazwsxedc."
}
```

**Response (Success):**

```json
{
  "token": "86eb3d31a8579246b218e8b212fb2c1c18f91921"
}
```

```json
{
  "token": "5e5bca06b04a849bea2c414e058a56ab0fd9ad17"
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
-d '{"username": "Festus", "password": "qazwsxedc.", "bio": "This is Festus's bio"}'
```

```bash
curl -X POST http://127.0.0.1:8000/api/accounts/register/ \
-H "Content-Type: application/json" \
-d '{"username": "Aboagye", "password": "qazwsxedc.", "bio": "This is Aboagye's bio"}'
```

**Login with Curl Example:**

```bash
curl -X POST http://127.0.0.1:8000/api/accounts/login/ \
-H "Content-Type: application/json" \
-d '{"username": "Festus", "password": "qazwsxedc."}'
```

```bash
curl -X POST http://127.0.0.1:8000/api/accounts/login/ \
-H "Content-Type: application/json" \
-d '{"username": "Aboagye", "password": "qazwsxedc."}'
```

Make sure to replace `newtuser` and `newpassword` with the actual user credentials during testing.

## 6. Implementing Posts and Comments Functionality

**Overview**
Users to manage posts and engage with them through comments in a social media platform by creating, viewing, updating, and deleting posts and comments. The API provides endpoints for managing these operations, with user authentication and permissions.

## Endpoints

### Posts

### Authentication

- The API requires authentication for creating, updating, and deleting posts and comments. Create a **user account using the Django Admin portal or python manage.py drf_create_token `<username>`** to generate token to access these features.

### Permissions

- Only the author of a post or comment can update or delete it.
- Anyone can view posts and comments.

### Testing

- All endpoints have been thoroughly tested using Postman.
- Example requests and responses are provided in this documentation to demonstrate the API’s functionality.

1. **Create a New Post**

- **URL:** `http://127.0.0.1:8000/posts/posts/`
- **Method**: `POST`
- **Authentication Required:** Yes
- **Description:** Allows authenticated users to create a new post.

**Request Body:**

```json
{
    "title": "First Post",
    "content": "What a journey to this point."
}
```

**Response:**

```json
{
    "id": 1,
    "author": "Festus",
    "title": "First Post",
    "content": "What a journey to this point.",
    "created_at": "2024-09-20T12:05:05.430148Z",
    "updated_at": "2024-09-20T12:05:05.430148Z"
}
```

2. **Retrieve a List of Post**

- **URL:** `http://127.0.0.1:8000/posts/posts/`
- **Method**: `GET`
- **Authentication Required:** No
- **Description:** Retrieve a list of all posts with pagination.

**Request Body:**

```json
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
          "id": 1,
          "author": "Festus",
          "title": "First Post",
          "content": "What a journey to this point.",
          "created_at": "2024-09-20T12:05:05.430148Z",
          "updated_at": "2024-09-20T12:05:05.430148Z"
      }
  ]
}
```

3. **Retrieve a Single Post**

- **URL:** `http://127.0.0.1:8000/posts/posts/1/`
- **Method**: `GET`
- **Authentication Required:** No
- **Description:** Retrieve a specific post by its ID..

**Request Body:**

```json
{
    "id": 1,
    "author": "Festus",
    "title": "First Post",
    "content": "What a journey to this point.",
    "created_at": "2024-09-20T12:05:05.430148Z",
    "updated_at": "2024-09-20T12:05:05.430148Z"
}
```

4. **Update a Post**

- **URL:** `http://127.0.0.1:8000/posts/posts/1/`
- **Method**: `PUT`
- **Authentication Required:** Yes
- **Description:** Allows the post's author to update the post.

**Request Body:**

```json
{
    "title": "First Post Updated",
    "content": "What a journey to this point."
}
```

**Response:**

```json
{
    "id": 1,
    "author": "Festus",
    "title": "First Post Updated",
    "content": "What a journey to this point and beyond.",
    "created_at": "2024-09-20T12:05:05.430148Z",
    "updated_at": "2024-09-20T12:14:45.893056Z"
}
```

5. **Delete a Post**

- **URL:** `http://127.0.0.1:8000/posts/posts/1/`
- **Method**: `DELETE`
- **Authentication Required:** Yes
- **Description:** Allows the post's author to delete the post.

**Response:**

```json
{
  "detail": "Post deleted successfully."
}
```

### Comments

1. **Create a New Comment**

- **URL:** `http://127.0.0.1:8000/posts/comments/`
- **Method**: `POST`
- **Authentication Required:** Yes
- **Description:** Allows authenticated users to add a comment to a post.

**Request Body:**

```json
{
    "post": 1,
    "content": "Congrats on making it this far.",
}
```

**Response:**

```json
{
    "id": 2,
    "post": 1,
    "author": "Aboagye",
    "content": "Congrats on making it this far.",
    "created_at": "2024-09-20T13:36:48.304820Z",
    "updated_at": "2024-09-20T13:36:48.304820Z"
}
```

2. **Retrieve a List of Comments**

- **URL:** `http://127.0.0.1:8000/posts/comments/`
- **Method**: `GET`
- **Authentication Required:** No
- **Description:** Retrieve a list of all comments with pagination.

**Request Body:**

```json
{
  "count": 2,
  "next": null,
  "previous": null,
  "results": [
      {
          "id": 1,
          "post": 1,
          "author": "Aboagye",
          "content": "Congrats on making it this far.",
          "created_at": "2024-09-20T12:17:08.356204Z",
          "updated_at": "2024-09-20T12:17:08.356204Z"
      },
      {
          "id": 2,
          "post": 1,
          "author": "Aboagye",
          "content": "Congrats on making it this far.",
          "created_at": "2024-09-20T13:36:48.304820Z",
          "updated_at": "2024-09-20T13:36:48.304820Z"
      }
  ]
}
```

3. **Retrieve a Single Comment**

- **URL:** `http://127.0.0.1:8000/posts/comments/1/`
- **Method**: `GET`
- **Authentication Required:** No
- **Description:** Retrieve a specific post by its ID..

**Request Body:**

```json
{
    "id": 1,
    "post": 1,
    "author": "Aboagye",
    "content": "Congrats on making it this far.",
    "created_at": "2024-09-20T12:17:08.356204Z",
    "updated_at": "2024-09-20T12:17:08.356204Z"
}
```

4. **Update a Comment**

- **URL:** `http://127.0.0.1:8000/posts/comments/1/`
- **Method**: `PUT`
- **Authentication Required:** Yes
- **Description:** Allows the comment's author to update the comment.

**Request Body:**

```json
{
    "post": 1,
    "content": "Slow but sure progress."
}
```

**Response:**

```json
{
    "id": 1,
    "post": 1,
    "author": "Aboagye",
    "content": "Slow but sure progress.",
    "created_at": "2024-09-20T12:17:08.356204Z",
    "updated_at": "2024-09-20T13:45:17.194217Z"
}
```

5. **Delete a Comment**

- **URL:** `http://127.0.0.1:8000/posts/posts/1/`
- **Method**: `DELETE`
- **Authentication Required:** Yes
- **Description:** Allows the comment's author to delete the comment.

**Response:**

```json
{
    "detail": "Comment deleted successfully."
}
```

## Filtering and Searching

### Filtering Posts

- You can filter posts by title using the query parameter `title`.

**Example Request:**

```perl
GET /posts/posts/?title=First%20Post #If deleted, use the one below.
GET /posts/posts/?title=First%20Post%20Updated
```

### Searching Posts

- You can search posts by `title` or `content` using the search query parameter.

**Example Request:**

```sql
GET /posts/posts/?search=content
```

### Pagination

- All list endpoints support pagination. The default page size is 5.

**Example Request:**

```bash
GET /posts/posts/?page=2
```

### Conclusion

This README provides all the necessary steps to set up the project, register and authenticate users, and interact with the API. For further details or contributions, feel free to create issues or submit pull requests on the repository.

**NOTE:**
Feel free to modify or expand this README as needed for your project!
