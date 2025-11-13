from django.contrib import admin
from .models import Uploader, Category, FoodImage, Question

class UploaderAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    search_fields = ('name', 'email')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','id')
    search_fields = ('name',)

class FoodImageAdmin(admin.ModelAdmin):
    list_display = ('uploader', 'upload_date', 'category')
    search_fields = ('uploader__name', 'category__name')
    list_filter = ('category', 'upload_date')

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'text')
    search_fields = ('text',)

admin.site.register(Uploader, UploaderAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(FoodImage, FoodImageAdmin)
admin.site.register(Question, QuestionAdmin)
