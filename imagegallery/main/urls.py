from django.urls import path
from . import views


urlpatterns = [
    path('', views.photos, name='photos'),
    path('contact', views.contact, name='contact'),
    path('photo/<str:title>', views.photo_detail, name='photo_detail'),
]