from django.urls import path
from .views import HomePageView, BasePageView

urlpatterns = [
    path('', BasePageView.as_view(), name='base'),
    path('home/', HomePageView.as_view(), name='home'),    
]