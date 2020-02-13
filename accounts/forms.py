from django.contrib.auth.forms import UserCreationForm

from django import forms 
from .models import User
from django.contrib.auth.forms import UserCreationForm


class UserAdminCreationform(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email']

    class UserAdminForm(forms.ModelForm):
        class Meta:
            model = User
            fields =  ['username', 'email', 'name', 'is_active', 'is_staff']