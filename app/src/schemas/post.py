from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field

from .user import User


class PostBase(BaseModel):
    first_phrase: str = Field(..., min_length=1, max_length=50, description="五音")
    second_phrase: str = Field(..., min_length=1, max_length=50, description="七音")
    third_phrase: str = Field(..., min_length=1, max_length=50, description="五音")


class Post(PostBase):
    id: int
    full_text: str
    note: Optional[str] = None
    season: Optional[str] = None
    kigo: Optional[str] = None
    posted_at: datetime
    created_at: datetime
    updated_at: datetime
    # 一時的に固定値を返す
    likes_count: int = 0
    comments_count: int = 0
    # ダミーユーザー情報
    user: User = User(id=1, name="俳句太郎", icon_url="/images/sample-icon.jpg")

    class Config:
        from_attributes = True


class PostList(BaseModel):
    total: int
    items: list[Post]
