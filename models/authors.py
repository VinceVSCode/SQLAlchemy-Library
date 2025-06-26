from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.base import Base

class Author(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key = True)
    name = Column(String, nullable = False)
    
    # Relationships
    books = relationship("Book", back_populates="author")
