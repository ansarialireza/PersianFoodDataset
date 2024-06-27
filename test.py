import os
import django

# تنظیمات Django را تنظیم کنید
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from django.db.models import Max
from dataset.models import FoodImage

def get_max_food_image_id():
    # کوئری برای یافتن بیشترین شناسه (id) FoodImage
    max_id = FoodImage.objects.aggregate(max_id=Max('id'))['max_id']
    
    # اگر رکوردی وجود داشت، بیشترین شناسه را برگردانید
    if max_id is not None:
        return max_id
    else:
        # اگر هیچ رکوردی پیدا نشد، عدد صفر را برگردانید
        return 0

if __name__ == "__main__":
    max_id = get_max_food_image_id()
    print(max_id)
