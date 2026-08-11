from typing import Annotated
import uuid
from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.service.explanation_service import (get_explanation_service, ExplanationService)
from app.db.session import get_async_session
from app.models.explanation import Explanation,ExplanationMode
from app.schemas.explanation import ExplanationCreate,ExplanationResponse,GeneratedExplanation


router = APIRouter(
    prefix="/explanations",
    tags=["Explanation"],
)

@router.post(
    "/",
    response_model=ExplanationResponse,
    status_code=status.HTTP_201_CREATED
)
async def create_explanation(
    user_id: uuid.UUID,
    data:ExplanationCreate,
    response:Response,
    explanation_service: ExplanationService = Depends(get_explanation_service),
) -> Explanation:
    return await explanation_service.create_explanation(
        user_id=user_id,
        data=data
    )

@router.get(
    "/{exp_id}",
    response_model=ExplanationResponse,
)
async def get_explanation_by_id(
    exp_id: uuid.UUID,
    explanation_service: ExplanationService = Depends(
        get_explanation_service
    ),
) -> Explanation:

    explanation = await explanation_service.get_explanation_by_id(exp_id)

    if explanation is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Explanation not found",
        )

    return explanation
    