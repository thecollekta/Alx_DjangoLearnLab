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

curl -X POST `http://localhost:8000/api/books/create/` -H "Authorization: Token YOUR_AUTH_TOKEN" -H "Content-Type: application/json" -d '{"title":"Book Title", "publication_year":2024, "author":1}'

### Retrieve a specific book

curl `http://localhost:8000/api/books/1/`

### Update a book

curl -X PUT `http://localhost:8000/api/books/update/` -H "Authorization: Token YOUR_AUTH_TOKEN" -H "Content-Type: application/json" -d '{"title":"Updated Book", "publication_year":2024, "author":1}'

### Delete a book

curl -X DELETE `http://localhost:8000/api/books/delete/` -H "Authorization: Token YOUR_AUTH_TOKEN"

## API Usage

### Book List Endpoint

The `/api/books/` endpoint supports filtering, searching, and ordering.

### Filtering

You can filter books by title, author, and publication year:
`/api/books/?title=Django&author=Festus&publication_year=2024`

### Searching

You can search books by title and author:
`/api/books/?search=Book+of+Rhymes`

### Ordering

You can order books by title, publication year, and author:
`/api/books/?ordering=-publication_year`

Use a minus sign (-) for descending order.

These features can be combined:
`/api/books/?search=Book+of+Rhymes&ordering=-publication_year&author__name=Festus`

## API Testing Strategy

### Test Cases

1. Retrieve book list
2. Retrieve book detail
3. Create new book (authenticated)
4. Update existing book (authenticated)
5. Delete book (authenticated)
6. Filter books
7. Search books
8. Order books
9. Verify authentication requirements

### Running Tests

To run the test suite:

1. Ensure you're in the project directory
2. Run: `python manage.py test api`

### Interpreting Results

- All tests should pass (OK)
- Any failures will be displayed with details about the failed assertion
- Check the output for any errors or failures and address them accordingly
