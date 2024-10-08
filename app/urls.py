from django.urls import path
from .views import HomePageView, AboutPageView, MintyPageView, ArtWorkPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('minty/', MintyPageView.as_view(), name='minty'),
    path('artwork/', ArtWorkPageView.as_view(), name='artwork'),
]
