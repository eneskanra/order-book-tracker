from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models

class ModelTests(TestCase):
    
    def test_book_str(self):
        """Test the book string representation"""
        pass