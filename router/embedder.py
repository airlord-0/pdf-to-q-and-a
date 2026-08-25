from google import genai 
from dotenv import load_dotenv


load_dotenv()

client = genai.Client()

def gem_embedder (chunks) :
    embedding = []
    
    for i, chunk in enumerate(chunks):
        result = client.models.embed_content (
            model= "gemini-embedding-2",
            contents = chunk,
        )
        print(chunk)
        embedding.append(result.embeddings[0])
    print("######## number of embeddings : ", len(embedding),"########")
    return embedding

