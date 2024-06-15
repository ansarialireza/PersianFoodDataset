from django import forms
from .models import Uploader, FoodImage
from django_recaptcha.fields import ReCaptchaField

class UploaderForm(forms.ModelForm):
    captcha = ReCaptchaField()

    class Meta:
        model = Uploader
        fields = ['name', 'email', 'captcha']

class FoodImageForm(forms.ModelForm):
    class Meta:
        model = FoodImage
        fields = ['image', 'category']
