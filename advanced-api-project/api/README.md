# API Endpoints

## Books

### List and Create Books

- URL: `/api/books/`
- Methods:
  - GET: List all books (no authentication required)
  - POST: Create a new book (authentication required)

### Retrieve, Update, and Delete Book

- URL: `/api/books/update/`
- URL: `/api/books/delete/`
- Methods:
  - GET: Retrieve a specific book (no authentication required)
  - PUT/PATCH: Update a specific book (authentication required)
  - DELETE: Delete a specific book (authentication required)

## Authentication

- Token-based authentication is used for protected endpoints.
- Include the token in the Authorization header:
  `Authorization: Token YOUR_AUTH_TOKEN`

## Testing the Views

### List all books (no authentication required)

curl `http://localhost:8000/api/books/`

### Create a new book

curl -X POST `http://localhost:8000/api/books/create/` -H "Authorization: Token YOUR_AUTH_TOKEN" -H "Content-Type: application/json" -d '{"title":"Boo", "publication_year":2024, "author":1}'

### Retrieve a specific book

curl `http://localhost:8000/api/books/1/`

### Update a book

curl -X PUT `http://localhost:8000/api/books/1/update/` -H "Authorization: Token YOUR_AUTH_TOKEN" -H "Content-Type: application/json" -d '{"title":"Updated Book", "publication_year":2024, "author":1}'

### Delete a book

curl -X DELETE `http://localhost:8000/api/books/1/delete/` -H "Authorization: Token YOUR_AUTH_TOKEN"
