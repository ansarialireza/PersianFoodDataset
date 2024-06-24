# food_images/utils.py

import os

def food_image_path(instance, filename):
    # instance is the instance of FoodImage being saved.
    # filename is the original filename of the uploaded file.
    
    # Get category name
    category_name = instance.category.name
    
    # Generate new filename (you can add more logic here if needed)
    new_filename = f"{category_name}_{instance.pk}_{filename}"
    
    # Add rating to the filename
    new_filename_with_rating = f"{new_filename}_rating{instance.rating}"
    
    # Return the path where the file will be uploaded
    return os.path.join('food_images', category_name, new_filename_with_rating)
