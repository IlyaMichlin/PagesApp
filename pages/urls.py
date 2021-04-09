from django.urls import path
from .views import HomePageView, AboupPageView


urlpatterns = [
    path('about/', AboupPageView.as_view(), name='about'),
    path('', HomePageView.as_view(), name='home'),
]
