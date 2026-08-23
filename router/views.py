from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import default_storage
from router.pdfExtractor import pdf_extractor
from router.chunker import text_splitter



# Create your views here.
# views in request - response module 
# othe frameworks call it actions 


def website (request):
    return render(request,'index.html')

# file upload page 
def uploaded (request):
    uploaded_file = request.FILES['uploaded-file']
    file_path = default_storage.save (
        uploaded_file.name, 
        uploaded_file
    )
    full_path=default_storage.path(file_path)
    print(full_path)
    text = pdf_extractor(full_path)
    print("################  here is the text \n")
    print(text)
    chunks = text_splitter(text,500,100)
    print(chunks)

    print (file_path)
    

    return HttpResponse(f"file uploaded successfully : {str(file_path)}")


