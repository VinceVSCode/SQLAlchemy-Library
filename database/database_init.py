from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config.paths import LIBRARY_DB_PATH
from models.base import Base

# Create an SQLite database engine. Print SQL statements for debugging.
engine = create_engine(f"sqlite:///{LIBRARY_DB_PATH}", echo=True)

# Create a session factory 
SessionLocal = sessionmaker(bind=engine)

# Function to create all tables in the database
def init_database():
    Base.metadata.create_all(bind=engine)
    print("Database created successfully!")
    