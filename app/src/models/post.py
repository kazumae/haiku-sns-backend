from sqlalchemy import Column, DateTime, Integer, String, Text
from sqlalchemy.sql import func

from ..database import Base


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)

    # 5-7-5の句を個別に保存
    first_phrase = Column(String(50), nullable=False, comment="五音")
    second_phrase = Column(String(50), nullable=False, comment="七音")
    third_phrase = Column(String(50), nullable=False, comment="五音")

    # 完全な俳句（表示用）
    full_text = Column(String(255), nullable=False, comment="完全な俳句")

    # 補足情報
    note = Column(Text, nullable=True, comment="補足説明、メモ等")

    # 季節情報
    season = Column(String(20), nullable=True, index=True, comment="季節")
    kigo = Column(String(50), nullable=True, index=True, comment="季語")

    # 投稿日時（俳句の作成日時）
    posted_at = Column(
        DateTime(timezone=True),
        nullable=False,
        comment="俳句の投稿日時",
    )

    # システム管理用のタイムスタンプ
    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
        comment="レコード作成日時",
    )
    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
        comment="レコード更新日時",
    )
