# File: schemas/schemas.py
from pydantic import BaseModel
# This file defines the schemas for the Book model using Pydantic.

class BookBase(BaseModel):
    title: str
    author: str

class BookCreate(BookBase):
    pass

class BookUpdate(BookBase):
    pass

class BookOut(BookBase):
    id: int

    
    class Config:
        orm_mode = True
    

    

