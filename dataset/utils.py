# utils.py

import os
from django.db.models import Max
from django.utils.text import get_valid_filename

def get_latest_id():
    from dataset.models import FoodImage
    max_id = FoodImage.objects.aggregate(max_id=Max('id'))['max_id']
    return max_id if max_id is not None else 0

def generate_filename(instance, filename):
    category_id = instance.category.id 
    rating = instance.rating
    unique_id = get_latest_id() + 1
    
    clean_filename = f"{category_id}_{rating}_{unique_id}.jpg"
    safe_filename = get_valid_filename(clean_filename)
    
    # Constructing the relative path
    final_path = os.path.join('food_images', safe_filename)
    
    return final_path

def food_image_path(instance, filename):
    return generate_filename(instance, filename)
