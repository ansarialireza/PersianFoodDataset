from django.db import models

class Uploader(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name

class FoodImage(models.Model):
    uploader = models.ForeignKey(Uploader, on_delete=models.CASCADE, related_name='foods')
    image = models.ImageField(upload_to='food_images/')
    upload_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='foods')
    
    def __str__(self):
        return self.uploader.name
