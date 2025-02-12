from typing import Any

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src import crud
from src.api import deps
from src.schemas.common import ListResponse
from src.schemas.post import Post

router = APIRouter()


@router.get("/", response_model=ListResponse[Post])
def get_posts(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    """
    俳句一覧を取得する
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
