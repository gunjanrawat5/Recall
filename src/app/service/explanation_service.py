from fastapi import Depends
from app.db.session import get_async_session
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
import uuid

from app.schemas import ExplanationResponse, ExplanationCreate, GeneratedExplanation
from app.models import Explanation
from app.service.llm_service import LLMService, get_llm_service

class ExplanationService:
    def __init__(self, db:AsyncSession, llm_service: LLMService) -> None:
            self.db = db
            self.llm_service = llm_service

    async def create_explanation(
        self,
        user_id: uuid.UUID,
        data: ExplanationCreate,
    ) -> Explanation:

        generated = await self.llm_service.generate_explanation(data)

        explanation = Explanation(
            user_id=user_id,

            selected_text=data.selected_text,
            surrounding_context=data.surrounding_context,
            page_title=data.page_title,
            page_url=data.page_url,
            mode=data.mode,

            summary=generated.content.summary,
            explanation=generated.content.explanation,
            key_points=generated.content.key_points,
            example=generated.content.example,
            analogy=generated.content.analogy,

            model_name=generated.model_name,
            input_tokens=generated.input_tokens,
            output_tokens=generated.output_tokens,
            latency_ms=generated.latency_ms,
        )

        self.db.add(explanation)
        await self.db.commit()
        await self.db.refresh(explanation)

        return explanation

    async def get_explanation_by_id(self, exp_id: uuid.UUID)-> Explanation | None:
        explanation =  await self.db.get(Explanation, exp_id)
        return explanation

def get_explanation_service(
            db: AsyncSession = Depends(get_async_session), llm_service: LLMService = Depends(get_llm_service)
    ) -> ExplanationService:
        return ExplanationService(db,llm_service)
