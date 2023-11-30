from django.urls import path
from .views import InventoryPageView

urlpatterns = [
    path('inventario/', InventoryPageView.as_view(), name='inventario'),
]