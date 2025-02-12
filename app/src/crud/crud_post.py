from typing import List, Tuple

from sqlalchemy.orm import Session

from src.models.post import Post


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
