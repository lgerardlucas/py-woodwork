from django.test import TestCase
from django.urls import reverse
from .models import TextureType

class List_TextureTypeTest(TestCase):
    def setUp(self):
        self.url = reverse('texturetype:list_texturetype')
    
    def test_response_200(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code,200)

    def test_template_used(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response,'list_texturetype.html')
    

class TextureTypeModelTest(TestCase):
    def test_saving_and_retrieving_Texture(self):
        first_item = TextureType()
        first_item.name = 'Lino teste 1'
        first_item.save()

        second_item = TextureType()
        second_item.name = 'Lino teste 2'
        second_item.save()

        saved_itens = TextureType.objects.all()
        self.assertEqual(saved_itens.count(),2)