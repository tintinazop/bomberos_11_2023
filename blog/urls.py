from django.urls import path
from .views import AboutPageView

urlpatterns = [
    path('blog/', AboutPageView.as_view(), name='about'),
]