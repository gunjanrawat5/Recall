import uuid

from pydantic import BaseModel, ConfigDict, Field


class PlayerCreate(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    team_number: int = Field(ge=1, le=99)


class PlayerResponse(BaseModel):
    id: uuid.UUID
    name: str
    team_number: int

    model_config = ConfigDict(from_attributes=True)