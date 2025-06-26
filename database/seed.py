from database.database_init import init_database, SessionLocal
from models import Author, Book, User, Loan
from datetime import datetime

# Function to seed the database with initial data
def seed_database():
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
        nitzsche = Author(name="Friedrich Nietzsche")

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
                             genre="Surreal", published_year=1915)
        thus_spoke_zarathustra = Book(title="Thus Spoke Zarathustra", author=nitzsche,
                                      genre="Philosophy", published_year=1885)
        
        # Create some users
        user1 = User(name="Mark", email="mark@example.com")
        user2 = User(name="Bob", email="bob@example.com")
        user3 = User(name="Joel", email="joel@example.com")

        # Create some loans
        loan1 = Loan(user=user1, book=hp1, borrowed_date=datetime.utcnow())
        loan2 = Loan(user=user2, book=metamorphosis, borrowed_date=datetime.utcnow())

        # add the data to the session
        session.add_all([
            rowling, tolkien, huxley, orwell, bradbury, kafka, nitzsche,
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
    
    finally:
        # Close the session
        session.close()
        print("Database seeded successfully!")

        
        
        
        