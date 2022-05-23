from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages

from .models import Photo
from .forms import MessageForm

# Create your views here.
site_url = 'http://127.0.0.1:8000'

def photos(request):
    query = request.GET.get('query')
    if query:
        photos = Photo.objects.filter(title__icontains=query)
    else:
        photos = Photo.objects.all()
    return render(request,'photos.html', {'photos': photos, 'site_url': site_url, 'query': query})

def contact(request):
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid:
            try:
                form.save()
                messages.success(request, "Your message has been sent!")
            except:
                messages.error(request, "Message could not be sent")
        else:
            messages.error(request, "Message could not be sent")
    form = MessageForm()
    return render(request,'contact.html', {'form': form})

def photo_detail(request, title):
    photo = get_object_or_404(Photo, title=title)
    photo.views += 1
    photo.save()
    
    latest_photos = Photo.objects.all().order_by('created_at')[:4]
    
    context = {
        'photo': photo,
        'latest_photos': latest_photos
    }
    return render(request, 'photo-detail.html', context)