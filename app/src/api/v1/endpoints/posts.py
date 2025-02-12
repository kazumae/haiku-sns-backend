from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src import crud
from src.api import deps
from src.schemas.common import ListResponse
from src.schemas.post import Post, PostBase

router = APIRouter()


@router.get("/", response_model=ListResponse[Post])
def get_posts(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    """
    俳句一覧を取得する（新しい順）
    """
    items, total = crud.get_posts(db, skip=skip, limit=limit)
    return {
        "paginate": {
            "total": total,
            "skip": skip,
            "limit": limit,
        },
        "items": items,
    }


@router.post("/", response_model=Post)
def create_post(
    *,
    db: Session = Depends(deps.get_db),
    post_in: PostBase,
) -> Any:
    """
    俳句を投稿する
    """
    return crud.create_post(db=db, obj_in=post_in)


@router.get("/{post_id}", response_model=Post)
def get_post(
    post_id: int,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    俳句の詳細を取得する
    """
    post = crud.get_post(db=db, post_id=post_id)
    if post is None:
        raise HTTPException(
            status_code=404,
            detail="俳句が見つかりません",
        )
    return post
