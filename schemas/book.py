from pydantic import BaseModel
# This file defines the schemas for model using Pydantic.

# Book schemas
class BookBase(BaseModel):
    title: str
    author_id: int
    genre: str
    published_year: int
    total_copies: int = 1

class BookCreate(BookBase):
    pass

class BookUpdate(BookBase):
    title: str | None = None
    author_id: int | None = None
    genre: str | None = None
    published_year: int | None = None
    total_copies: int | None = None
    is_available: bool | None = None

class BookOut(BookBase):
    id: int
    is_available: bool
    
    class Config:
        from_attributes = True