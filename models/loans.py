from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime 
from models.base import Base

class Loan(Base):
    __tablename__ = "loans"

    id = Column(Integer, primary_key=True)
    book_id = Column(Integer, ForeignKey("books.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    borrowed_date = Column(DateTime, default= datetime.utcnow, nullable=False)  
    returned_date = Column(DateTime, nullable=True)  

    # Relationships
    book = relationship("Book", back_populates="loans")
    user = relationship("User", back_populates="loans")

    def __repr__(self):
        return (
            f"<Loan(id={self.id}, book_id={self.book_id}, user_id={self.user_id}"
            f", borrowed_date={self.borrowed_date}"
            f", returned_date={self.returned_date})>"
            )