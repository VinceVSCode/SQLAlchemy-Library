from database.database_init import SessionLocal
from models import User, Book, Loan

# Open a session
session = SessionLocal()

# 1. List all books
print("📚 All books:")
for book in session.query(Book).all():
    #Get attribute to check availability
    print(f" - {book.title} ({'Available' if getattr(book, 'is_available', False) else 'Borrowed'})")

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
