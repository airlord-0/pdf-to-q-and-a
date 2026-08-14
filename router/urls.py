from django.urls import path
from router import views


#url config
urlpatterns = [
    path('',views.website),
    path('uploaded/',views.uploaded)
]