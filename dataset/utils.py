import os
from django.db.models import Max
from django.conf import settings

def get_latest_id():
    from dataset.models import FoodImage
    max_id = FoodImage.objects.aggregate(max_id=Max('id'))['max_id']
    return max_id if max_id is not None else 0

def generate_filename(instance, filename):
    category_name = instance.category.name
    rating = instance.rating
    unique_id = get_latest_id() + 1
    
    new_filename = f"{rating}_{unique_id}.jpg"
    return os.path.join(settings.MEDIA_ROOT, 'food_images', category_name, new_filename)

def food_image_path(instance, filename):
    return generate_filename(instance, filename)
