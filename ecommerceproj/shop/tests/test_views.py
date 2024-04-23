from django.test import TestCase,Client
from django.urls import reverse

# class TestViews(TestCase):
#     def test_home(self):
#         client=Client()
#         response=client.get(reverse('home'))
#         print(response)
#         self.assertEqual(response.status_code,200)
#         self.assertTemplateUsed(response,'home.html')

# class TestViews(TestCase):
#     def test_signin(self):
#         client=Client()
#         response=client.get(reverse('signin'))
#         print(response)
#         self.assertEqual(response.status_code,200)
#         self.assertTemplateUsed(response,'signin.html')


class Testhomeviews(TestCase):

    def setUp(self):
        self.client=Client()
        self.home=reverse('home')
        self.cart=reverse('cart')

    def test_home_View(self):
        response= self.client.get(self.home)
        print("Response is: ", response)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'home.html')

    def test_cart_views(self):
        response = self.client.get(self.cart)
        print("Response is: ", response)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cart.html')