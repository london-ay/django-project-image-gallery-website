import email
from email import message
from unicodedata import name
from django.db import models

# Create your models here.
class Photo(models.Model):
    created_at = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=64)
    photo = models.ImageField()
    views = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.title
    
class Message(models.Model):
    created_at = models.DateField(auto_now_add=True)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    
    def __str__(self):
        return f"Message by {self.email}"