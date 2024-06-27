import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()
from dataset.models import FoodImage
from django.db.models import Max

def get_max_food_image_id():
    # کوئری برای یافتن بیشترین شناسه (id) FoodImage
    max_id = FoodImage.objects.aggregate(max_id=Max('id'))['max_id']
    
    # اگر رکوردی وجود داشت، بیشترین شناسه را برگردانید
    if max_id is not None:
        return max_id
    else:
        # اگر هیچ رکوردی پیدا نشد، عدد صفر را برگردانید
        return 0

def food_image_path(instance, filename):
    # instance is the instance of FoodImage being saved.
    # filename is the original filename of the uploaded file.
    
    # Get category name
    category_name = instance.category.name
    
    # Get the rating
    rating = instance.rating
    
    # Generate a unique numerical identifier
    unique_id = get_max_food_image_id()+1
    
    # Generate new filename
    new_filename = f"{rating}_{unique_id}.jpg"
    
    # Return the path where the file will be uploaded
    return os.path.join('food_images', category_name, new_filename)
