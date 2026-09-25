from google import genai
from dotenv import load_dotenv



load_dotenv()

client = genai.Client()

def generate_answer (llm_feed) : 
    result = client.models.generate_content (
                model= "gemini-3.5-flash-lite",
                contents = llm_feed
            )
    print(result.text)

