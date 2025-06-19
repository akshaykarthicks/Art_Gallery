from django import forms
from .models import Image

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image']
        labels = {'image': 'Upload Image'}

    def save(self):
        image = Image(image=self.cleaned_data['image'])
        image.save()
        return image 
            