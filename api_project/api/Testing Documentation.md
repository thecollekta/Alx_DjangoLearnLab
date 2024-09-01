# Testing Documentation for CRUD Operations on Book API

## Overview

This documentation provides instructions for testing the CRUD (Create, Read, Update, Delete) operations on the Book model API using Django REST Framework's ViewSets and Routers. The tests will be conducted using Postman, a popular REST client, and will focus on three African books.

## Prerequisites

- Django project `api_project` set up with Django REST Framework.
- Book model implemented in `api/models.py`.
- `BookViewSet` implemented in `api/views.py`.
- Router configuration in `api/urls.py`.

## Test Data

**Books:**

1. **"Things Fall Apart" by Chinua Achebe**
2. **"Half of a Yellow Sun" by Chimamanda Ngozi Adichie**
3. **"Purple Hibiscus" by Chimamanda Ngozi Adichie**

## Step 1: Testing the Create Operation

To create new book entries in the database:

- **Endpoint:** `POST /api/books/`
- **Headers:**
  - `Content-Type: application/json`
- **Request Body:**

  ```json
  {
    "title": "Things Fall Apart",
    "author": "Chinua Achebe"
  }
  ```

  ```json
  {
    "title": "Half of a Yellow Sun",
    "author": "Chimamanda Ngozi Adichie"
  }
  ```

  ```json
  {
    "title": "Purple Hibiscus",
    "author": "Chimamanda Ngozi Adichie"
  }
  ```

- **Expected Response:**
  - **Status Code:** `201 Created`
  - **Response Body:**

    ```json
    {
      "id": 1,
      "title": "Things Fall Apart",
      "author": "Chinua Achebe"
    }
    ```

## Step 2: Testing the Read Operation

To retrieve the list of all books:

- **Endpoint:** `GET /api/books/`
- **Headers:** None required.
- **Expected Response:**
  - **Status Code:** `200 OK`
  - **Response Body:**

    ```json
    [
      {
        "id": 1,
        "title": "Things Fall Apart",
        "author": "Chinua Achebe"
      },
      {
        "id": 2,
        "title": "Half of a Yellow Sun",
        "author": "Chimamanda Ngozi Adichie"
      },
      {
        "id": 3,
        "title": "Purple Hibiscus",
        "author": "Chimamanda Ngozi Adichie"
      }
    ]
    ```

To retrieve a single book by ID:

- **Endpoint:** `GET /api/books/1/`
- **Headers:** None required.
- **Expected Response:**
  - **Status Code:** `200 OK`
  - **Response Body:**

    ```json
    {
      "id": 1,
      "title": "Things Fall Apart",
      "author": "Chinua Achebe"
    }
    ```

## Step 3: Testing the Update Operation

To update a book's details:

- **Endpoint:** `PUT /api/books/1/`
- **Headers:**
  - `Content-Type: application/json`
- **Request Body:**

  ```json
  {
    "title": "Things Fall Apart - Updated",
    "author": "Chinua Achebe"
  }
  ```
  
- **Expected Response:**
  - **Status Code:** `200 OK`
  - **Response Body:**

    ```json
    {
      "id": 1,
      "title": "Things Fall Apart - Updated",
      "author": "Chinua Achebe"
    }
    ```

## Step 4: Testing the Delete Operation

To delete a book:

- **Endpoint:** `DELETE /api/books/1/`
- **Headers:** None required.
- **Expected Response:**
  - **Status Code:** `204 No Content`
  - **Response Body:** Empty

## Final Notes

- Ensure to test each operation in the specified order: Create, Read, Update, and Delete.
- For full CRUD coverage, repeat the process with different book IDs.
- For any failed tests, check the Django console for error logs.

This documentation follows best practices to ensure comprehensive API testing, providing both expected responses and specific instructions to validate the implementation of CRUD operations on the Book model API.
