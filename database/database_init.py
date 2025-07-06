from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base
from config.paths import LIBRARY_DB_PATH, DB_URL
from models.base import Base

# Create an SQLite database engine. Print SQL statements for debugging.
# engine = create_engine(f"sqlite:///{LIBRARY_DB_PATH}", echo=True)
engine = create_engine(DB_URL, echo=True)

# Create a session factory 
SessionLocal = sessionmaker(bind=engine)

# Create a base class for declarative models
Base = declarative_base()

# Function to create all tables in the database
def init_database():
    Base.metadata.create_all(bind=engine)
    print("Database created successfully!")
    