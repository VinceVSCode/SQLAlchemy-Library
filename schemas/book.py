from pydantic import BaseModel, EmailStr
# This file defines the schemas for model using Pydantic.

# Book schemas
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