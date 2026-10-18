from django.test import TestCase
from django.urls import reverse

from labs.models import Product


class ProductFormLatihanTest(TestCase):
    def test_valid_post_creates_product(self):
        response = self.client.post(
            reverse("latihan:product_create"),
            {"name": "Monitor", "stock": 5, "price": 2500000},
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Product.objects.filter(name="Monitor").exists())

    def test_invalid_post_shows_validation_errors(self):
        response = self.client.post(
            reverse("latihan:product_create"),
            {"name": "", "stock": -1, "price": -5},
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "errorlist")
        self.assertEqual(Product.objects.count(), 0)
