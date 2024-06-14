from django.views.generic import TemplateView
from dataset.models import Category
class Index(TemplateView):
    template_name='website/index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context