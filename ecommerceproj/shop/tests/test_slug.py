from django.test import TestCase
from django.urls import reverse,resolve
from shop.views import home

class TestUrl(TestCase):
    def test_url_slug(self):
        url=reverse('product_by_category',args=['demo_slug'])
        print(resolve(url))
        self.assertEqual(resolve(url).func,home)


