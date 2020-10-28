from pydantic import BaseModel

from ..abstract import Base


class UserCreate(BaseModel):
    name: str


class User(Base):
    name: str

    class Config:
        orm_mode = True
