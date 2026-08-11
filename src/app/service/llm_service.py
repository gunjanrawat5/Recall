from google import genai
from google.genai import types
import time
from app.core.config import settings
from app.schemas import ExplanationCreate, GeneratedExplanation, LLMResult

class LLMService:

    def __init__(self) -> None:
        self.client = genai.Client(api_key=settings.gemini_api_key)


    async def generate_explanation(self, data:ExplanationCreate) -> LLMResult:

        prompt = self._build_prompt(data)
        start = time.perf_counter()
        response = await self.client.aio.models.generate_content(
            model="gemini-3.1-flash-lite",
            contents=prompt,
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
                response_schema=GeneratedExplanation,
            ),
        )

        latency_ms = int((time.perf_counter() - start)*1000)

        if response.parsed is None:
            raise ValueError("Gemini did not return a valid structured response")

        content = GeneratedExplanation.model_validate(response.parsed)
        return LLMResult(
            content=content,
            model_name="gemini-3.1-flash-lite",
            input_tokens=(
                response.usage_metadata.prompt_token_count
                if response.usage_metadata
                else None
            ),
            output_tokens=(
                response.usage_metadata.candidates_token_count
                if response.usage_metadata
                else None
            ),
            latency_ms=latency_ms,
        )

    def _build_prompt(self,data:ExplanationCreate) -> str:
         return f"""
            You are an educational assistant.

            Explain the selected text according to the requested explanation mode.

            MODE:
            {data.mode.value}

            SELECTED TEXT:
            {data.selected_text}

            SURROUNDING CONTEXT:
            {data.surrounding_context or "No additional context provided."}

            PAGE TITLE:
            {data.page_title or "Unknown"}

            Return a useful educational explanation.

            Guidelines:
            - summary should be short and clear
            - explanation should explain the concept thoroughly
            - key_points should contain the most important takeaways
            - example should be included when useful
            - analogy should be included when useful
            """

def get_llm_service() -> LLMService:
        return LLMService()