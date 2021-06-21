from django.test import TestCase
from django.urls import reverse

class List_FurnitureTest(TestCase):
    def setUp(self):
        self.url = reverse('furniture:list_furniture')
    
    def test_response_200(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code,200)

    def test_template_used(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response,'list_furniture.html')