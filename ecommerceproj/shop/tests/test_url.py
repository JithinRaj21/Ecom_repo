from django.test import TestCase

class TestUrl(TestCase):
    def test_homepage(self):
        result=self.client.get('/')
        print(result)
        self.assertEqual(result.status_code,200)



