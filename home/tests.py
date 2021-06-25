from django.test import TestCase
from django.urls import reverse, resolve
from django.http import HttpRequest
from .views import home

class HomeTest(TestCase):
    def setUp(self):
        self.url = reverse('home:home')
    
    def test_response_200(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code,200)

    def test_template_used(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response,'home.html')
        
    def test_home_page_return_corret_html(self):
        request = HttpRequest()
        response = home(request)
        html = response.content.decode('utf8')
        self.assertTrue('<html>' in html)
        self.assertTrue('</html>' in html)
        self.assertTrue('WoodWork' in html)

