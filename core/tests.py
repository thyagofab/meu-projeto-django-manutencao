from django.test import TestCase
from django.urls import reverse


class HomeViewTest(TestCase):

    def test_home_status_code(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    def test_home_response(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(
            response.json()["message"],
            "Olá, Django!"
        )
