
import uuid
from fastapi import APIRouter, Depends, HTTPException, Response, status
from app.service.explanation_service import (get_explanation_service, ExplanationService)
from app.models.explanation import Explanation
from app.schemas.explanation import ExplanationCreate,ExplanationResponse
from app.core.security.current_user import get_current_user
from app.models.user import User


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
    data:ExplanationCreate,
    current_user: User = Depends(get_current_user),
    explanation_service: ExplanationService = Depends(get_explanation_service),
) -> Explanation:
    return await explanation_service.create_explanation(
        user_id=current_user.id,
        data=data
    )

@router.get(
    "/{exp_id}",
    response_model=ExplanationResponse,
)
async def get_explanation_by_id(
    exp_id: uuid.UUID,
    current_user: User = Depends(get_current_user),
    explanation_service: ExplanationService = Depends(
        get_explanation_service
    ),
) -> Explanation:

    explanation = await explanation_service.get_explanation_by_id(exp_id, user_id=current_user.id)

    if explanation is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Explanation not found",
        )

    return explanation

@router.get(
    "",
    response_model=list[ExplanationResponse]
)
async def get_explanations(
    current_user:User = Depends(get_current_user),
    explanation_service: ExplanationService = Depends(get_explanation_service)
) -> list[Explanation]:
    return await explanation_service.get_explanations(current_user.id)
    