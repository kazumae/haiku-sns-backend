from pydantic import BaseModel


class UserBase(BaseModel):
    name: str
    icon_url: str


class User(UserBase):
    id: int

    class Config:
        from_attributes = True
