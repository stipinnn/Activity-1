from django.shortcuts import render
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'app/home.html'

class AboutPageView(TemplateView):
    template_name = 'app/about.html'
    
class MintyPageView(TemplateView):
    template_name = 'app/minty.html'

class ArtWorkPageView(TemplateView):
    template_name = 'app/artwork.html'
