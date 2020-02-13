
from django.urls import path
#from django.views.generic.edit import CreateView
from .views import RegisterCreate, IndexView



urlpatterns = [
    path('', IndexView.as_view(), name='index.html'),
    path('register', RegisterCreate.as_view(), name='register.html'),
]