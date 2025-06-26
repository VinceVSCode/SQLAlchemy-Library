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
    
    # Relationships
    author = relationship("Author", back_populates="books")
    loans = relationship("Loan", back_populates="book")
    
    def __repr__(self):
        return f"<Book(id={self.id}, title='{self.title}', author_id={self.author_id})>"
    