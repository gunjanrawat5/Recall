import uuid
import datetime
from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field

from app.models.explanation import ExplanationMode


class ExplanationCreate(BaseModel):
    user_id: uuid.UUID
    selected_text: str = Field(min_length=1)
    surrounding_context: str | None = None
    page_title: str | None = None
    page_url : str | None = None
    mode: ExplanationMode

class GeneratedExplanation(BaseModel):
    summary: str = Field(min_length=1)
    explanation: str = Field(min_length=1)
    key_points:list[str] = Field(default_factory=list)
    example:str | None = None
    analogy: str | None = None

class ExplanationResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: uuid.UUID
    selected_text: str = Field(min_length=1)
    surrounding_context: str | None = None
    page_title: str | None = None
    page_url : str | None = None
    mode: ExplanationMode
    summary: str = Field(min_length=1)
    explanation: str = Field(min_length=1)
    key_points:list[str] = Field(default_factory=list)
    example:str | None = None
    analogy: str | None = None
    created_at: datetime

