"""LLM integration used by the question-and-answer endpoint."""

from google import genai
from dotenv import load_dotenv

load_dotenv()


def answer_question(question: str) -> str:
    """Generate a text answer for a non-empty user question."""
    client = genai.Client()
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=question,
    )

    answer = getattr(response, "text", None)
    if not answer:
        raise RuntimeError("The LLM returned no text.")
    return answer
