from django.urls import path
from router import views


#url config
urlpatterns = [
    path('namaste/',views.greetings),
    path('afternoon/',views.say_hello),
    path('myweb/',views.website)
]