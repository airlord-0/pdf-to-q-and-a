from router.chunker import text_splitter
from router.embedder import gem_embedder
from router.database import get_index


def context_generator (user_question) :
    

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
    results = get_index().query (vector = question_vector,
            top_k = 3, 
            include_metadata = True)
    print("********** here are the results **********")
    print(results.matches)
    # access matching chunks 
    print("*********the for loop ***********")
    context = []
    for match in response['matches'] : 
        print(f"Score: {match['score']}")       # Similarity score
        print(f"Text: {match['metadata']['text']}")
        context.append(match['metadata']['text'])
    promtp =f"""
        You are a PDF question-answering assistant.
    Use the provided context to answer the user's question.
    Context:
    {context}
    Question:
    {user_question}
    Answer the question using the context above.
    If the answer cannot be found in the context, say that the information is not available in the document.
    """
    return promtp