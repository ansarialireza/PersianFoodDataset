from django import forms
from .models import Uploader, FoodImage
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV2Invisible

class UploaderForm(forms.ModelForm):

    class Meta:
        model = Uploader
        fields = ['name', 'email',]

class FoodImageForm(forms.ModelForm):
    captcha = ReCaptchaField()
    class Meta:
        model = FoodImage
        fields = ['image', 'category','rating']
