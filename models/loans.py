from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime ,timedelta
from models.base import Base

class Loan(Base):
    __tablename__ = "loans"

    id = Column(Integer, primary_key=True)
    book_id = Column(Integer, ForeignKey("books.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    borrowed_date = Column(DateTime, default= datetime.utcnow, nullable=False)  
    returned_date = Column(DateTime, nullable=True)  

    def __repr__(self):
        return (
            f"<Loan(id={self.id}, book_id={self.book_id}, user_id={self.user_id}"
            f", borrowed_date={self.borrowed_date}"
            f", returned_date={self.returned_date})>"
            )
    
    @property
    def can_extend(self):
        return self.returned_date is None and not hasattr(self, '_extended')
    
    @property
    def extend_due_date(self, days=7):
        # Check if the loan can be extended
        if not self.can_extend:
            return False
        self._extended = True
        self.borrowed_date += timedelta(days=days)
        return True

    # Relationships
    book = relationship("Book", back_populates="loans")
    user = relationship("User", back_populates="loans")