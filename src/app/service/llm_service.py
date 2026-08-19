from google import genai
from google.genai import types
import time
from app.core.config import settings
from app.schemas import ExplanationCreate, GeneratedExplanation, LLMResult
from app.models.explanation import ExplanationMode

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

    def _build_prompt(self, data: ExplanationCreate) -> str:
            mode_instructions = self._get_mode_instructions(data.mode)

            return f"""
        You are an educational assistant.

        Your job is to explain the selected text accurately using the surrounding context.

        SELECTED TEXT:
        {data.selected_text}

        SURROUNDING CONTEXT:
        {data.surrounding_context or "No additional context provided."}

        PAGE TITLE:
        {data.page_title or "Unknown"}

        EXPLANATION MODE:
        {data.mode.value}

        MODE-SPECIFIC INSTRUCTIONS:
        {mode_instructions}

        GENERAL REQUIREMENTS:
        - Stay faithful to the selected text and surrounding context.
        - Do not invent facts that are not supported by the text or general established knowledge.
        - Define important technical terms when necessary.
        - Prefer clarity over unnecessary jargon.
        - Make the explanation self-contained.
        - Avoid repeating the same idea across summary, explanation, key points, example, and analogy.
    """

    def _get_mode_instructions(
        self,
        mode: ExplanationMode,
    ) -> str:

        if mode == ExplanationMode.CONCISE:
            return """
    - Give a very short explanation.
    - Focus only on the core meaning.
    - Keep the explanation to roughly 2-4 sentences.
    - Return 2-3 key points.
    - Only include an example or analogy if it significantly improves understanding.
    """

        if mode == ExplanationMode.BEGINNER:
            return """
    - Assume the reader has little or no prior knowledge.
    - Explain unfamiliar terminology in simple language.
    - Build the idea from basic concepts before introducing technical details.
    - Use a concrete example.
    - Use an intuitive analogy when appropriate.
    - Return 3-5 key points.
    """

        if mode == ExplanationMode.DETAILED:
            return """
    - Give a thorough technical explanation.
    - Explain how and why the concept works, not only what it means.
    - Include relevant mechanisms, relationships, or underlying concepts.
    - Clarify important terminology.
    - Mention useful nuances or limitations when relevant.
    - Include a concrete example.
    - Return 4-7 key points.
    """

        raise ValueError(f"Unsupported explanation mode: {mode}")
    
def get_llm_service() -> LLMService:
        return LLMService()