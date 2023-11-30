from django.views.generic import TemplateView, ListView

class BasePageView(TemplateView):
    template_name = 'main/base.html'

class HomePageView(TemplateView):
    template_name = 'main/home.html'
