from sqlalchemy import Column, Integer, String
from datetime import datetime
from sqlalchemy.orm import relationship
from models.base import Base

class User(Base):
    __tablename__ = "users"

    # User fields
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    
    # Relationships
    loans = relationship("Loan", back_populates="user")
