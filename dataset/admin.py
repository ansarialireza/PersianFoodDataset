from django.contrib import admin
from .models import Uploader, Category, FoodImage

class UploaderAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    search_fields = ('name', 'email')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class FoodImageAdmin(admin.ModelAdmin):
    list_display = ('uploader', 'upload_date', 'category')
    search_fields = ('uploader__name', 'category__name')
    list_filter = ('category', 'upload_date')

admin.site.register(Uploader, UploaderAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(FoodImage, FoodImageAdmin)
