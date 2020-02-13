
from django.urls import path
#from django.views.generic.edit import CreateView
from .views import RegisterCreate, IndexView


from . import views


urlpatterns = [
    path('', IndexView.as_view(), name='index.html'),
    path('register', views.RegisterCreate.as_view(), name='register.html'),
]