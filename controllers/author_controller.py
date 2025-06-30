from database.database_init import SessionLocal
from models import Author


def add_author(name: str):
    session = SessionLocal()
    try:
        existing = session.query(Author).filter_by(name=name).first()
        if existing:
            print(f"❗ Author '{name}' already exists.")
            return
        author = Author(name=name)
        session.add(author)
        session.commit()
        print(f"✅ Author '{name}' added.")
    finally:
        session.close()


def list_authors():
    session = SessionLocal()
    try:
        authors = session.query(Author).all()
        if not authors:
            print("⚠️ No authors found.")
        for author in authors:
            print(f" - {author.name}")
    finally:
        session.close()
