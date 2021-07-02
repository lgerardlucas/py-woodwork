from django.test import TestCase
from django.urls import reverse
from .models import Furniture

class List_FurnitureTest(TestCase):
    def setUp(self):
        self.url = reverse('furniture:list_furniture')
    
    def test_response_200(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code,200)

    def test_template_used(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response,'list_furniture.html')

class FurnitureModelTest(TestCase):
    def test_saving_and_retrieving_Texture(self):
        first_item = Furniture()
        first_item.name = 'Mesa'
        first_item.save()

        second_item = Furniture()
        second_item.name = 'Porta'
        second_item.save()

        saved_itens = Furniture.objects.all()
        self.assertEqual(saved_itens.count(),2)                        