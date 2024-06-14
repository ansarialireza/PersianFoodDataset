from django.urls import path
from .views import *
from . import views


app_name = 'website'

urlpatterns=[
    path('',Index.as_view(),name='index'),
    
]