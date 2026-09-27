from google import genai
from dotenv import load_dotenv



load_dotenv()

client = genai.Client()

def generate_answer (prompt) : 
    result = client.models.generate_content (
                model= "gemini-3.5-flash-lite",
                contents = prompt
            )
    return result.text

