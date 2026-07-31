from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.
# views in request - response module 
# othe frameworks call it actions 

def greetings(request):
    return HttpResponse("good morning pavan")

def say_hello(request):
    return HttpResponse("hello world")

def website (request):
    return render(request,'index.html')