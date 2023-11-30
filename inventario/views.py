from django.views.generic import TemplateView, ListView
from .models import Movement

class InventoryPageView(ListView):
    model = Movement
    template_name = 'inventario.html'