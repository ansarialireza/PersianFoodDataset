from django.db import models

class Food(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='food_images/')
    upload_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name