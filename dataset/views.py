from django.shortcuts import render, redirect
from .forms import UploaderForm, FoodImageForm

def upload_image(request):
    if request.method == 'POST':
        uploader_form = UploaderForm(request.POST)
        food_image_form = FoodImageForm(request.POST, request.FILES)
        if uploader_form.is_valid() and food_image_form.is_valid():
            uploader = uploader_form.save()
            food_image = food_image_form.save(commit=False)
            food_image.uploader = uploader
            food_image.save()
            return redirect('success')
    else:
        uploader_form = UploaderForm()
        food_image_form = FoodImageForm()
    return render(request, 'upload_image.html', {
        'uploader_form': uploader_form,
        'food_image_form': food_image_form,
    })

def success(request):
    return render(request, 'success.html')
