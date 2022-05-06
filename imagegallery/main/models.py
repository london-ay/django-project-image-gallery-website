from django.db import models

# Create your models here.
class Photo(models.Model):
    created_at = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=64)
    photo = models.ImageField()
    
    def __str__(self):
        return self.title