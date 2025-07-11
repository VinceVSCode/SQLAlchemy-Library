# Dynamically add project root to sys.path. when directly run this file.
import sys 
from pathlib import Path
# Ensure the root directory is in the system path
ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT_DIR))

# Import necessary modules and classes
from database.database_init import init_database, SessionLocal
from models.authors import Author
from models.books import Book
from models.users import User
from models.loans import Loan

from datetime import datetime,timedelta
from config.paths import DB_URL

# Suppress warnings for cleaner output
import warnings
warnings.filterwarnings('ignore')


# Function to seed the database with initial data
def seed_database():
    print(f"📂 Seeding database at: {DB_URL}")
    # Create the tables
    init_database() 
    session = SessionLocal()

    try:
        
        rowling = Author(name="J.K. Rowling")
        tolkien = Author(name="J.R.R. Tolkien")
        huxley = Author(name="Aldous Huxley")
        orwell = Author(name="George Orwell")
        bradbury = Author(name="Ray Bradbury")
        kafka = Author(name="Franz Kafka")
        nietzsche = Author(name="Friedrich Nietzsche")

        # Create some books
        hp1 = Book(title="Harry Potter and the Sorcerer's Stone", author=rowling,
                   genre="Fantasy", published_year=1997)
        hobbit = Book(title="The Hobbit", author=tolkien,
                      genre="Fantasy", published_year=1937)
        brave_new_world = Book(title="Brave New World", author=huxley,
                               genre="Dystopian", published_year=1932)
        nineteen_eighty_four = Book(title="1984", author=orwell,
                                    genre="Dystopian", published_year=1949)
        fahrenheit_451 = Book(title="Fahrenheit 451", author=bradbury,
                                 genre="Dystopian", published_year=1953)
        metamorphosis = Book(title="The Metamorphosis", author=kafka,
                             genre="Surreal", published_year=1915, total_copies=2)
        thus_spoke_zarathustra = Book(title="Thus Spoke Zarathustra", author=nietzsche,
                                      genre="Philosophy", published_year=1885, total_copies=3)
        
        # Create some users
        user1 = User(username="Mark", email="mark@example.com")
        user2 = User(username="Bob", email="bob@example.com")
        user3 = User(username="Joel", email="joel@example.com")

        # Create some loans
        loan1 = Loan(
        user=user1,
        book=hp1,
        borrowed_date=datetime.utcnow(),
        returned_date=datetime.utcnow() + timedelta(days=14)  
        )

        loan2 = Loan(
                    user=user2, 
                    book=metamorphosis,
                    borrowed_date=datetime.utcnow(),
                    returned_date= datetime.utcnow() + timedelta(days=14)  
                    )

        # add the data to the session
        session.add_all([
            rowling, tolkien, huxley, orwell, bradbury, kafka, nietzsche,
            hp1, hobbit, brave_new_world, nineteen_eighty_four,
            fahrenheit_451, metamorphosis, thus_spoke_zarathustra,
            user1, user2, user3,
            loan1, loan2
        ])
        # commit current session
        session.commit()
    except Exception as e:
        # Rollback the session in case of error
        session.rollback()
        print(f"An error occurred while seeding the database: {e}")
        raise e  # Re-raise to see the full traceback
    
    finally:
        # Close the session
        session.close()
        print("Database seeded successfully!")

        
if __name__ == "__main__":
    seed_database()
    print("Seeding complete!")
        
        