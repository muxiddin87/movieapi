
from django.test import TestCase, Client
from ..models import Movie

class TestMovieViewSet(TestCase):
    def setUp(self) -> None:
        self.movie = Movie.objects.create(name="Test Movies")
        self.client = Client()

    def test_get_all_movies(self):
        response = self.client.get('/movies/')
        data = response.data

        self.assertEquals(response.status_code, 200)
        self.assertEquals(len(data), 1)
        self.assertIsNotNone(data[0]["id"])
        self.assertEquals(data[0]["name"], "Test Movies")


    def test_search(self):
        response = self.client.get('/movies/?search=Test Movies')
        data = response.data

        self.assertEquals(response.status_code, 200)
        self.assertEquals(len(data), 1)
        self.assertEquals(data[0]["name"], "Test Movies")

    def test_ordering(self):
        response = self.client.get('/movies/?ordering=Test Name')
        data = response.data

        self.assertEquals(response.status_code, 200)
        self.assertEquals(len(data), 1)
        self.assertEquals(data[0]["name"], "Test Movies")


