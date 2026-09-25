from django.shortcuts import render
import json

from django.http import HttpResponse, JsonResponse
from django.core.files.storage import default_storage
from django.views.decorators.http import require_POST



# Create your views here.
# views in request - response module 
# othe frameworks call it actions 


def website (request):
    return render(request,'index.html')


def generate_answer(question):
    """Import the LLM integration only when an answer is requested."""
    from router.llm import answer_question

    return answer_question(question)


# file upload page 
def uploaded (request):
    from router.pdfExtractor import pdf_extractor
    from router.chunker import text_splitter
    from router.embedder import gem_embedder
    from router.database import vectorbase_upsert

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


@require_POST
def answer(request):
    """Return an LLM answer as JSON for the question form on the home page."""
    try:
        payload = json.loads(request.body or "{}")
    except json.JSONDecodeError:
        return JsonResponse({"error": "The request body must be valid JSON."}, status=400)

    question = payload.get("question", "").strip()
    if not question:
        return JsonResponse({"error": "Please enter a question."}, status=400)

    try:
        generated_answer = generate_answer(question)
    except Exception:
        return JsonResponse(
            {"error": "Unable to generate an answer right now. Please try again."},
            status=502,
        )

    return JsonResponse({"answer": generated_answer})
