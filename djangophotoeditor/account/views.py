from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.


class IndexView(TemplateView):
    template_name = 'account/index.html'


class PhotosView(TemplateView):
    template_name = 'account/photo.html'
