from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('errorpage', views.errorpage),
    path('contact', views.contact)
    
]