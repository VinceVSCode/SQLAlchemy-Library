# A script to demonstrate the use of filters in SQLAlchemy queries.

#Find all the books in fantasy genre
from services import filters

print("📚 Fantasy Books:")
for book in filters.get_books_by_genre("Fantasy"):
    print(f" - {book.title}")

print("\n📖 Books Published Before 1950:")
for book in filters.get_books_before_year(1950):
    print(f" - {book.title} ({book.published_year})")

print("\n👥 Users with Gmail Accounts:")
for user in filters.get_users_with_email_domain("gmail.com"):
    print(f" - {user.name} ({user.email})")

print("\n📕 Books by 'Orwell':")
for book in filters.get_books_by_author("Orwell"):
    print(f" - {book.title} by {book.author.name}")

print("\n📗 Books with 'the' in Title:")
for book in filters.get_books_by_substring("the"):
    print(f" - {book.title}")
