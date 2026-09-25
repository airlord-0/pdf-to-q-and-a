from django.http import JsonResponse 
from django.shortcuts import render # to display my page
from django.core.files.storage import default_storage 
from router.pdfExtractor import pdf_extractor
from router.chunker import text_splitter
from router.embedder import gem_embedder
from router.database import vectorbase_upsert
from router.retriver import similarToQuestion
from router.llm import generate_answer

def home(request) :
    return render(request,"index.html") 

def uploaded(request) :
    
    # get the uploaded file name and print it 
    uploaded_file = request.FILES['uploaded-file']
    file_path = default_storage.save(
        uploaded_file.name,
        uploaded_file
    )
    full_path = default_storage.path(file_path)
    print(full_path)
    print("pdf recieved ", uploaded_file.name)

     # extract the text out of the pdf
    text = pdf_extractor(full_path)
    print(text)

     # chunk these text into smaller units 
    unit,metadatas = text_splitter(text,500,100)

     # convert units into embeddings 
    vectors = gem_embedder(unit)
    print(vectors)

     # upsert units, embeddings and metadata to the pinecone mah
    doc_id = 1
    batch_size = 100
    vectorbase_upsert(unit,vectors,metadatas,doc_id,batch_size)



    return JsonResponse({
        "server says" : f"{uploaded_file.name} uploaded successfully "
    })


def questions(request) :
    # get the user question from the server and print it 

    questions = request.POST['question']
    print("question received ", questions)
    
    

    Llmfeed = similarToQuestion(questions)

    answer =generate_answer(Llmfeed)


    return JsonResponse ({
        "bot" : answer
    })
     