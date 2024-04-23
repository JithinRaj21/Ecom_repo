from django.test import TestCase
from shop.models import *

class TestModel(TestCase):
    def test_category(self):
        category1=Category.objects.create(name= 'Home and Living',slug='home',desc='demo')
        self.assertEqual(str(category1),'Home and Living')
        print('Isinstance:',isinstance(category1,Category))
        self.assertTrue(isinstance(category1,Category))

