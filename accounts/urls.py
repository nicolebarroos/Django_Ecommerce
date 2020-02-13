
from django.urls import path
#from django.views.generic.edit import CreateView
from .views import RegisterCreate, InicioView, RegisterUpdate, ModifyPassword

app_name = 'accounts'

urlpatterns = [
    path('', InicioView.as_view(), name='index.html'),
    path('register', RegisterCreate.as_view(), name='register.html'),
    path('update', RegisterUpdate.as_view(), name='update_user.html'),
    path('modify', ModifyPassword.as_view(), name='update_password.html')
]