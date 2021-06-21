from django.test import TestCase
from django.urls import reverse

class HomeTest(TestCase):
    def setUp(self):
        self.url = reverse('home:home')

        def test_reponse_200(self):
            response = self.client.get(self.url)
            self.assertEqual(response.status_code,200)
        
        def test_template_uset(sefl):
            response = self.client.get(self.url)
            self.assertTemplateUsed(response,'home.html')

