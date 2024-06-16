from django.views.generic import TemplateView
from dataset.models import Category
from django.conf import settings

class Index(TemplateView):
    template_name = 'website/index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['site_key'] = settings.RECAPTCHA_PUBLIC_KEY
        return context
