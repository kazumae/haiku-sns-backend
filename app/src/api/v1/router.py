from fastapi import APIRouter

from src.api.v1.endpoints import posts

from .endpoints import tests

api_router = APIRouter()
api_router.include_router(tests.router, prefix="/tests", tags=["テスト"])
api_router.include_router(posts.router, prefix="/posts", tags=["俳句"])
