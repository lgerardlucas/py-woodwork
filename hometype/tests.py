from django.test import TestCase
from django.urls import reverse

class New_HomeTypeTest(TestCase):
    def setUp(self):
        self.url = reverse('hometype:new_hometype')
    
    def test_response_200(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code,200)

    def test_template_used(self):
        response = self.client.get(self.url)
        
        self.assertTemplateUsed(response,'new_hometype.html')