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

def get_users_with_email_domain(domain: str):
    """Fetch all users with a specific email domain."""
    session = SessionLocal()
    if not domain.startswith('@'):
        print("Please provide a valid email domain starting with '@'.")
        return []
    try:
        pattersn = f"%{domain}"
        users = session.query(User).filter(User.email.like(pattersn)).all()
        if not users:
            print(f"No users found with the email domain: {domain}")
        else:
            print(f"Found {len(users)} user(s) with the email domain: {domain}")
        return users
    except Exception as e:
        print(f"Error fetching users: {e}")
        return []
    finally:
        session.close()