from django.shortcuts import render
#from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    CreateView, UpdateView, FormView, TemplateView
)
#from django.views.generic import TemplateView

from accounts.models import User
from .forms import UserAdminCreationform
from django.urls import reverse_lazy



class IndexView(TemplateView):

    template_name = 'accounts/index.html'


class RegisterCreate(CreateView):
    model = User
    template_name = 'accounts/register.html'
    form_class = UserAdminCreationform
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = User.objects.all()[:5]
        return context
    