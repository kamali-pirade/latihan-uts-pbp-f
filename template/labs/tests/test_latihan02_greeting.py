from django.test import TestCase
from django.urls import reverse


class GreetingLatihanTest(TestCase):
    def test_name_from_url_is_rendered_by_template(self):
        response = self.client.get(reverse("latihan:greeting", args=["Budi"]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Halo, Budi!")

    def test_different_url_argument_changes_the_output(self):
        response = self.client.get(reverse("latihan:greeting", args=["Alya"]))
        self.assertContains(response, "Halo, Alya!")
