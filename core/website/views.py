from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView
from django.shortcuts import redirect
from django.contrib import messages
from dataset.forms import UploaderForm, FoodImageForm
from dataset.models import Category
from django.conf import settings
from dataset.models import *
class UploadImageView(FormView):
    template_name = 'website/index.html'
    form_class = UploaderForm
    second_form_class = FoodImageForm
    success_url = reverse_lazy('website:index')

    def get_context_data(self, **kwargs):
        context = super(UploadImageView, self).get_context_data(**kwargs)
        context['uploader_form'] = self.form_class()
        context['food_image_form'] = self.second_form_class()
        question = Question.objects.first()
        context['question'] = question
        context['categories'] = Category.objects.all()
        context['site_key'] = settings.RECAPTCHA_PUBLIC_KEY
        return context

    def post(self, request, *args, **kwargs):
        self.object = None
        print("Request POST data:", request.POST)
        print("Request FILES data:", request.FILES)
        uploader_form = self.form_class(request.POST)
        food_image_form = self.second_form_class(request.POST, request.FILES)
        print("Uploader form valid:", uploader_form.is_valid())
        print("Uploader form errors:", uploader_form.errors)
        print("Food image form valid:", food_image_form.is_valid())
        print("Food image form errors:", food_image_form.errors)
        if uploader_form.is_valid() and food_image_form.is_valid():
            return self.form_valid(uploader_form, food_image_form)
        else:
            return self.form_invalid(uploader_form, food_image_form)

    def form_valid(self, uploader_form, food_image_form):
        uploader = uploader_form.save()
        food_image = food_image_form.save(commit=False)
        food_image.uploader = uploader
        food_image.save()
        messages.success(self.request, 'Form submitted successfully!')
        return redirect(self.success_url)

    def form_invalid(self, uploader_form, food_image_form):
        messages.error(self.request, 'Form submission failed. Please correct the errors.')
        context = self.get_context_data()
        context['uploader_form'] = uploader_form
        context['food_image_form'] = food_image_form
        return self.render_to_response(context)

class SuccessView(TemplateView):
    template_name = 'website/index.html'  # Change template_name to the appropriate value for SuccessView

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        messages.success(self.request, 'Form submitted successfully!')
        return context
