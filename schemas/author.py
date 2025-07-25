from pydantic import BaseModel


class AuthorBase(BaseModel):
    name: str


class AuthorCreate(AuthorBase):
    pass


class AuthorOut(AuthorBase):
    id: int

    class Config:
        from_attributes = True