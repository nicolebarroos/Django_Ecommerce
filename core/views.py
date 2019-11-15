from django.shortcuts import render
from django.views.generic import View, TemplateView, CreateView

class IndexView(TemplateView):
    template_name = 'index.html'

index = IndexView.as_view()
