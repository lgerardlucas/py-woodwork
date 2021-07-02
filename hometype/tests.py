from django.test import TestCase
from django.urls import reverse
from .models import HomeType

class List_HomeTypeTest(TestCase):
    def setUp(self):
        self.url = reverse('hometype:list_hometype')
    
    def test_response_200(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code,200)

    def test_template_used(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response,'list_hometype.html')

class HomeTypeModelTest(TestCase):
    def test_saving_and_retrieving_Texture(self):
        first_item = HomeType()
        first_item.name = 'Casa'
        first_item.save()

        second_item = HomeType()
        second_item.name = 'Apartamento'
        second_item.save()

        saved_itens = HomeType.objects.all()
        self.assertEqual(saved_itens.count(),2)                