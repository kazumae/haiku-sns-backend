from datetime import datetime
from typing import List, Optional, Tuple

from sqlalchemy.orm import Session

from src.models.post import Post
from src.schemas.post import PostBase


def get_posts(db: Session, skip: int = 0, limit: int = 100) -> Tuple[List[Post], int]:
    """
    俳句の一覧を取得する

    Args:
        db: データベースセッション
        skip: スキップする件数
        limit: 取得する最大件数

    Returns:
        Tuple[List[Post], int]: 俳句のリストと総件数
    """
    # 総件数を取得
    total = db.query(Post).count()

    # 一覧を取得
    items = (
        db.query(Post).order_by(Post.posted_at.desc()).offset(skip).limit(limit).all()
    )

    return items, total


def create_post(db: Session, *, obj_in: PostBase) -> Post:
    """
    俳句を作成する

    Args:
        db: データベースセッション
        obj_in: 作成する俳句のデータ

    Returns:
        Post: 作成された俳句
    """
    # 完全な俳句テキストを生成
    full_text = f"{obj_in.first_phrase} {obj_in.second_phrase} {obj_in.third_phrase}"

    db_obj = Post(
        first_phrase=obj_in.first_phrase,
        second_phrase=obj_in.second_phrase,
        third_phrase=obj_in.third_phrase,
        full_text=full_text,
        posted_at=datetime.now(),
    )
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def get_post(db: Session, post_id: int) -> Optional[Post]:
    """
    指定されたIDの俳句を取得する

    Args:
        db: データベースセッション
        post_id: 俳句ID

    Returns:
        Optional[Post]: 俳句が存在する場合はPostオブジェクト、存在しない場合はNone
    """
    return db.query(Post).filter(Post.id == post_id).first()
