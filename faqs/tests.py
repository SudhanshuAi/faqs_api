# faqs/tests.py

import pytest
from django.test import TestCase
from rest_framework.test import APITestCase
from .models import FAQ

class FAQModelTests(TestCase):
    def setUp(self):
        self.faq = FAQ.objects.create(
            question="Test Question",
            answer="Test Answer"
        )

    def test_translation_caching(self):
        translated = self.faq.get_translated_content(lang='hi')
        self.assertIsNotNone(translated['question'])
        
class FAQAPITests(APITestCase):
    def test_faq_list_api(self):
        response = self.client.get('/api/faqs/')
        self.assertEqual(response.status_code, 200)