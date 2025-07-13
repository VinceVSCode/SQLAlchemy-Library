from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from models.base import Base


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    author_id = Column(Integer, ForeignKey("authors.id"), nullable=False)
    genre = Column(String, nullable=False)
    published_year = Column(Integer, nullable=False)
    is_available = Column(Boolean, default=True)  
    total_copies = Column(Integer, default=1, nullable=False)
    
    # Relationships
    author = relationship("Author", back_populates="books")
    loans = relationship("Loan", back_populates="book")
    
    def __repr__(self):
        return f"<Book(id={self.id}, title='{self.title}', author_id={self.author_id})>"
    
    # Property to count borrowed books
    @property
    def borrowed_count(self):
        return sum(1 for loan in self.loans if loan.returned_date is None)
    
    # Property to check if the book is available
    @property
    def available_copies(self) -> int:
        # Calculate available copies by subtracting borrowed count from total copies else return 0
        total_copies = getattr(self, "total_copies", 0)
        return max(int(total_copies) - int(self.borrowed_count), 0)
