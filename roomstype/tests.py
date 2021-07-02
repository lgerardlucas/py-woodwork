from django.test import TestCase
from django.urls import reverse
from .models import RoomsType

class List_RoomsTypeTest(TestCase):
    def setUp(self):
        self.url = reverse('roomstype:list_roomstype')
    
    def test_response_200(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code,200)

    def test_template_used(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response,'list_roomstype.html')

class RoomsTypeModelTest(TestCase):
    def test_saving_and_retrieving_Texture(self):
        first_item = RoomsType()
        first_item.name = 'Sala'
        first_item.save()

        second_item = RoomsType()
        second_item.name = 'Cozinha'
        second_item.save()

        saved_itens = RoomsType.objects.all()
        self.assertEqual(saved_itens.count(),2)        