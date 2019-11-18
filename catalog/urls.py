#from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
    path('product_list/', views.product_list, name='product_list'),
    path('category<slug>/', views.category, name='category'),
    path('product/<slug:title>/', views.product, name='product'),
]