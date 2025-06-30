from database.database_init import SessionLocal
from models import User


def add_user(name: str, email: str):
    session = SessionLocal()
    try:
        existing = session.query(User).filter_by(email=email).first()
        if existing:
            print(f"❗ A user with email '{email}' already exists.")
            return
        user = User(name=name, email=email)
        session.add(user)
        session.commit()
        print(f"✅ User '{name}' added.")
    finally:
        session.close()


def list_users():
    session = SessionLocal()
    try:
        users = session.query(User).all()
        if not users:
            print("⚠️ No users found.")
        for user in users:
            print(f" - {user.name} ({user.email})")
    finally:
        session.close()
