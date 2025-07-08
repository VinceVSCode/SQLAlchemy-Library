from pydantic import BaseModel, EmailStr, Field
# This file defines the schemas for model using Pydantic.

# User schemas
class UserBase(BaseModel):
    username: str = Field(..., min_length=3, max_length=20, description="The username of the user. Must be between 3 and 20 characters.")
    email: EmailStr

# UserCreate schema
class UserCreate(UserBase):
    password: str

#UserOut returning user data
class UserOut(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True