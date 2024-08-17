# retrieve.md

# Retrieve Book
>>> ...
>>> book = Book.objects.get(id=1)
print(book.title, book.author, book.publication_year)
# Output: 1984 George Orwell 1949