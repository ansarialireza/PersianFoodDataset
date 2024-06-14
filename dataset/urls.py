from django.urls import path
from .views import *

app_name = 'dataset'

urlpatterns = [
    path('upload/',UploadImageView.as_view(), name='upload_image'),
    path('success/',SuccessView.as_view(), name='success'),
]
