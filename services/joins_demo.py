from services.joins import get_borrowed_books_with_users

# This is a demo service to show how to use the joins service.
print("📚 Borrowed Books:")
for loan in get_borrowed_books_with_users():
    book = loan.book
    user = loan.user
    print(f" - '{book.title}' borrowed by {user.name} on {loan.borrowed_date}")
print("📚 End of borrowed books list.")