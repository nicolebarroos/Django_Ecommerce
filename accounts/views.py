from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    CreateView, UpdateView, FormView, TemplateView
)
#from django.contrib.auth.views import login as auth_login
from accounts.models import User
from .forms import UserAdminCreationform
from django.contrib.auth.forms import PasswordChangeForm
from django.urls import reverse_lazy



class IndexView(TemplateView):

    template_name = 'accounts/index.html'


class RegisterCreate(CreateView):
    model = User
    template_name = 'accounts/register.html'
    form_class = UserAdminCreationform
    success_url = reverse_lazy('index')

    #def get_context_data(self, **kwargs):
    #    context = super().get_context_data(**kwargs)
    #    context['user'] = User.objects.all()[:5]
    #    return context

class RegisterUpdate(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'accounts/update_user.html'
    fields = ['name', 'email']
    success_url = reverse_lazy('index')

    def get_object(self):
        return self.request.user

class ModifyPassword(LoginRequiredMixin, FormView):
    template_name = 'accounts/update_password.html'
    success_url = reverse_lazy('index')
    form_class = PasswordChangeForm

    def get_form_kwargs(self):
        kwargs = super(ModifyPassword, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.save()
        return super(ModifyPassword, self). form_valid(form)

    
index = IndexView.as_view()
register = RegisterCreate.as_view()
update_user = RegisterUpdate.as_view()
update_password = ModifyPassword.as_view()