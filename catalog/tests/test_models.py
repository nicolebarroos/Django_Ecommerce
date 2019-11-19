from django.test import TestCase
from django.urls import reverse

from model_bakery import baker

from catalog.models import Category, Product

class CategoryTestCase(TestCase):

    def setUp(self):
        self.category = baker.make('catalog.Category')

    def test_get_absolute_url(self):
        self.assertEquals(
            self.category.get_absolute_url(),
            reverse('catalog:category', kwargs={'slug': self.category.slug})

        )

    def ProductTestCase(TestCase):
        def setUp(self):
            self.product = baker.make(Product, slug='produto')

        def test_get_absolute_url(self):
            self.assertEquals(
                self.product.test_get_absolute_url(),
                reverse('catalog:product', kwargs={'slug': 'produto'})
            )




