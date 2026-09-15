from django.urls import path
from router import views


#url config
urlpatterns = [
    path('',views.home),
    path('uploaded/',views.uploaded, name="uploaded"),
    path('questions/',views.questions,name = "questions")
    
]