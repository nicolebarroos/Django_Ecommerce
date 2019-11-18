from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.db import models
from django.views.decorators.cache import cache_page

from .models import Product, Category


#O django-watson é um rápido plug-in de pesquisa de texto completo com vários modelos para o Django
from watson import search as watson


class ProductListView(generic.ListView):
    template_name = 'catalog/product_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        queryset = Product.objects.all()
        q = self.request.GET.get('q', '')
        if q:
            queryset = watson.filter(queryset, q)
        return queryset

product_list = ProductListView.as_view()

class CategoryListView(generic.ListView):
    template_name = 'catalog/category.html'
    context_object_name = 'product_list'

    def get_queryset(self):
        return Product.objects.filter(category_slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        context['current_category'] = get_object_or_404(Category, slug=self.kwargs['slug'])
        return context

category = CategoryListView.as_view()

@cache_page(60 * 10)
def product(request, slug):
    product = Product.objects.get(slug=slug)
    context = {
        'product': product
    }
    return render(request, 'catalog/product.html', context)