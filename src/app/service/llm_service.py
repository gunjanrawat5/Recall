from app.schemas import ExplanationCreate, GeneratedExplanation

from fastapi import Depends
from app.db.session import get_async_session
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


class LLMService:
    def __init__(self, db : AsyncSession) -> None:
        self.db = db

    async def generate_explanation(self, data:ExplanationCreate) -> GeneratedExplanation:
        return GeneratedExplanation(
            summary="Temporary summary",
            explanation="Temporary explanation",
            key_points=[
                "Temporary point 1",
                "Temporary point 2",
            ],
            example=None,
            analogy=None,
        )