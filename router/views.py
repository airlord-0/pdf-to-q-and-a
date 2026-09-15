from django.http import JsonResponse 
from django.shortcuts import render # to display my page
from django.core.files.storage import default_storage 

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

    return JsonResponse({
        "server says" : f"{uploaded_file.name} uploaded successfully "
    })

def questions(request) :
    # get the user question from the server and print it 

    questions = request.POST['question']
    print("question received ", questions)

    return JsonResponse ({
        "answer" : f"{questions} has been received  "
    })

     