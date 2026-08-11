# src/app/api/router.py

from fastapi import APIRouter

from app.api.routes.players import router as players_router
from app.api.routes.users import router as users_router
from app.api.routes.explanation import router as explanation_router

api_router = APIRouter()

api_router.include_router(users_router)
api_router.include_router(players_router)
api_router.include_router(explanation_router)
