from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from .utils import food_image_path 

class Uploader(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name

class FoodImage(models.Model):
    uploader = models.ForeignKey(Uploader, on_delete=models.CASCADE, related_name='foods')
    image = models.ImageField(upload_to=food_image_path)
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
