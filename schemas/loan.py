from datetime import datetime
from pydantic import BaseModel


class LoanBase(BaseModel):
    user_id: int
    book_id: int


class LoanCreate(LoanBase):
    pass


class LoanOut(LoanBase):
    id: int
    borrowed_date: datetime
    returned_date: datetime | None

    class Config:
        from_attributes = True