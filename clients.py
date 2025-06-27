from database.database_init import SessionLocal
from models import User, Book, Loan

# Open a session
session = SessionLocal()

# 1. List all books
print("📚 All books:")
for book in session.query(Book).all():
    # Display book title and available copies
    if book.available_copies > 0:
        print(f" - {book.title} ({book.available_copies} of {book.total_copies} available)")
    else:
        print(f" - {book.title} (No copies available)")
# 2. Show all borrowed books
print("\n📕 Borrowed books:")
for loan in session.query(Loan).filter(Loan.returned_date == None).all():
    print(f" - {loan.book.title} borrowed by {loan.user.name} on {loan.borrowed_date}")

# 3. List users and how many books they borrowed
print("\n👤 Users and their loan count:")
for user in session.query(User).all():
    print(f" - {user.name}: {len(user.loans)} loan(s)")

# Close the session
session.close()
