from django.db import models
import os

def get_upload_path(instance, filename):
    return os.path.join('images', filename)

class Image(models.Model):
    image = models.ImageField(upload_to=get_upload_path)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.image)
    
    
    
    