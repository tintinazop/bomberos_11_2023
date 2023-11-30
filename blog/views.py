from django.views.generic import TemplateView, ListView
from .models import Post

class AboutPageView(ListView):
    model = Post
    template_name = 'about.html'