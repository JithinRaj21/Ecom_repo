from django.test import TestCase
from django.urls import reverse, resolve
from shop.views import *


class TestUrl(TestCase):
    def test_homepage(self):
        url = reverse('home')
        print('Url is:', url)
        self.assertEqual(resolve(url).func, home)
        self.assertTemplateUsed('home.html')
        print(resolve(url))















class TestUrl(TestCase):
    def test_cartpage(self):
        url = reverse('cart')
        print('Url is:', url)
        self.assertEqual(resolve(url).func, show_cart)
        self.assertTemplateUsed('cart.html')
        print(resolve(url))