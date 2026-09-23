from router.chunker import text_splitter
from router.embedder import gem_embedder
from router.database import get_index


def similarToQuestion (user_question) :
    

    question_chunks, _ = text_splitter(user_question)
    question_embeddings = gem_embedder(question_chunks)
    question_vector = list(question_embeddings[0].values)
    
    # I need not upsert the question embeddings to the database 
    # just check for similar chunks 

    # query the index for most similar chunks 
    response = get_index().query (
        vector = question_vector,
        top_k = 3, 
        include_metadata = True
        
    )
    # access matching chunks 
    for match in response['matches'] : 
        print(f"Score: {match['score']}")       # Similarity score
        print(f"Text: {match['metadata']['text']}")
