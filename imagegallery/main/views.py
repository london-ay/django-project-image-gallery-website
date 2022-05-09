from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

from .models import Photo

# Create your views here.
site_url = 'http://127.0.0.1:8000'

def home(request):
    query = request.GET.get('query')
    if query:
        photos = Photo.objects.filter(title__icontains=query)
    else:
        photos = Photo.objects.all()
    return render(request,'home.html', {'photos': photos, 'site_url': site_url, 'query': query})
#HttpResponse('<h1 style= "background-color: pink; " > My Portfolio  is here! </h1>')

def errorpage(request):
    return HttpResponse ('<h2 style= "background-color: red; ">This is an error page I decided.</h2>', status=404)

def contact(request):
    return HttpResponse('<h2 style= "background-color: lightblue; ">My contact number is 07900039390. I don"t like being contacted.</h2>')

