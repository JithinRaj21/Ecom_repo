from django.test import TestCase

# Create your tests here.

# def demo(str1,str2):
#     return str1 + str2
# class test_str(TestCase):
#     def test_concate(self):
#         self.assertEqual(demo('hello','world'),'helloworld')

def get_max(num1,num2):
    return num1 if num1>num2 else num2
class Testdemo(TestCase):
    def test_get_max(self):
        self.assertEqual(get_max(5,7),7)