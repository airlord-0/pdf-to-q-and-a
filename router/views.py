from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import default_storage
from router.pdfExtractor import pdf_extractor
from router.chunker import text_splitter
from router.embedder import gem_embedder
from router.database import vectorbase_upsert



# Create your views here.
# views in request - response module 
# othe frameworks call it actions 


def website (request):
    return render(request,'index.html')

# file upload page 
def uploaded (request):
    # get the file path
    uploaded_file = request.FILES['uploaded-file']
    file_path = default_storage.save (
        uploaded_file.name, 
        uploaded_file
    )
    # store the file path
    full_path=default_storage.path(file_path)
    print(full_path)

    # extract the text from the pdf
    text = pdf_extractor(full_path)

    # check whats been extracted
    print("################  here is the text \n")
    print(text)

   # break the extracted document into smaller pieces
    unit,metadatas= text_splitter(text,500,100) # the function is first returning the units then metadata
    

    # pass chunks to embedder -> convert into word embeddings 
    vectors = gem_embedder(unit)
    print(vectors)


    # store embeddings and units as with other metadata as a record 
    doc_id = 1
    batch_size = 100
    vectorbase_upsert(unit,vectors,metadatas,doc_id,batch_size)

    

    return HttpResponse(f"file uploaded successfully : {str(file_path)}")

  
