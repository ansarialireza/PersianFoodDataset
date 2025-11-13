# models.py
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from .utils import food_image_path 
from django.core.exceptions import ValidationError

class Uploader(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    
    def __str__(self):
        return self.name

class Category(models.Model):
    id = models.IntegerField(primary_key=True) 
    name = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name


def validate_image_file_extension(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.jpg', '.jpeg', '.png', '.gif']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')

class FoodImage(models.Model):
    uploader = models.ForeignKey(Uploader, on_delete=models.CASCADE, related_name='foods')
    image = models.ImageField(upload_to=food_image_path, validators=[validate_image_file_extension])
    upload_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='foods')
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )

    def __str__(self):
        return f"Uploader: {self.uploader.name}, Category: {self.category.name}"

class Question(models.Model):
    text = models.CharField(max_length=255)
    
    def __str__(self):
        return self.text
