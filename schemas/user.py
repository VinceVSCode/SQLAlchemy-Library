from pydantic import BaseModel, EmailStr
# This file defines the schemas for model using Pydantic.

# User schemas
class UserBase(BaseModel):
    username: str
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