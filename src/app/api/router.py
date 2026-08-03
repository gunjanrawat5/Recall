# src/app/api/router.py

from fastapi import APIRouter

from app.api.routes.players import router as players_router

api_router = APIRouter()

api_router.include_router(players_router)