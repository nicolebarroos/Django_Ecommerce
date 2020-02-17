
from django.urls import path
#from django.views.generic.edit import CreateView
from .views import RegisterCreate, IndexView, RegisterUpdate, ModifyPassword
from . import views


app_name = 'accounts'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('register', RegisterCreate.as_view(), name='register.html'),
    path('update', views.RegisterUpdate.as_view(), name='update_user'),
    path('modify', views.ModifyPassword.as_view(), name='update_password')
]