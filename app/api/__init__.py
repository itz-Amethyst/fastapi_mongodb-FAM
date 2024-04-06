from fastapi import APIRouter
from app.api import document
router = APIRouter(
    prefix = '/api',
)

router.include_router(document.router)