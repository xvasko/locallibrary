from django.test import TestCase
from catalog.models import Genre

class GenreTestCase(TestCase):

    def setUp(self):
        self.genre = Genre.objects.create(name='Test Genre')

    def test_genre_str(self):
        self.assertEqual(str(self.genre), 'Test Genre')
