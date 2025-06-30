from services.joins import get_borrowed_books_with_users, get_users_and_their_books

# This is a demo service to show how to use the joins service.
print("📚 Borrowed Books:")
for loan in get_borrowed_books_with_users():
    book = loan.book
    user = loan.user
    print(f" - '{book.title}' borrowed by {user.name} on {loan.borrowed_date}")
print("📚 End of borrowed books list.")

# Now, let's also show users and their active loans
for user in get_users_and_their_books():
    books = [loan.book.title for loan in user.loans if loan.returned_date is None]
    print(f" - {user.name}: {books or 'No active loans'}")