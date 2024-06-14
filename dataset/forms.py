from django import forms
from .models import Uploader, FoodImage

class UploaderForm(forms.ModelForm):
    class Meta:
        model = Uploader
        fields = ['name', 'email']

class FoodImageForm(forms.ModelForm):
    class Meta:
        model = FoodImage
        fields = ['image', 'category']
