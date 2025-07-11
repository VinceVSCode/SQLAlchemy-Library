from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from models.base import Base

class User(Base):
    __tablename__ = "users"

    # User fields
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index = True, nullable=False)
    email = Column(String, unique=True ,index = True, nullable=False)
    is_active = Column (Boolean, default=True)
    
    # Relationships
    loans = relationship("Loan", back_populates="user")

    def __repr__(self):
        return f"<User(id={self.id}, name='{self.username}', email='{self.email}')>"