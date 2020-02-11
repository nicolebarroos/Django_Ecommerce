from django.shortcuts import render
#from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    CreateView, TemplateView, UpdateView, FormView
)


class IndexView(TemplateView):

    template_name = 'accounts/index.html'