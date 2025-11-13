from django.urls import path
from .views import *
from . import views


app_name = 'website'

urlpatterns=[
    path('',UploadImageView.as_view(),name='index'),
    
]