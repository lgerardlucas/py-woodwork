from django.test import TestCase
from django.urls import reverse
from .models import Register

class RegisterTest(TestCase):
    def setUp(self):
        self.url = reverse('register:register')