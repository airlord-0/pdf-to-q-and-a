from pinecone import Pinecone 
from dotenv import load_dotenv
load_dotenv ()

pc = Pinecone()
index = pc.Index("context")

# make a function that takes units, embeddings, metadata