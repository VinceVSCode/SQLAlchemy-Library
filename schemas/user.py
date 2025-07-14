from pydantic import BaseModel, EmailStr, Field
# This file defines the schemas for model using Pydantic.

# User schemas
class UserBase(BaseModel):
    username: str = Field(..., min_length=3, max_length=20)
    email: EmailStr

# UserCreate schema
class UserCreate(UserBase):
    password: str

#UserOut returning user data
class UserOut(UserBase):
    id: int
    is_active: bool

    class Config:
        from_attributes = True

#UserUpdate updating user data
class UserUpdate(BaseModel):
    username: str | None = Field(None, min_length=3, max_length=20)
    email: EmailStr | None = None
    is_active: bool | None = None

# UserInDB schema for internal use
class UserInDB(UserBase):
    id: int
    is_active: bool

    class Config:
        from_attributes = True