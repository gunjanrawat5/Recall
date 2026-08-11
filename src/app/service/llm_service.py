from app.schemas import ExplanationCreate, GeneratedExplanation

class LLMService:
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

def get_llm_service() -> LLMService:
        return LLMService()