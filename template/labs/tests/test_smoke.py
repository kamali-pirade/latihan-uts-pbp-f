from django.test import TestCase
from django.urls import reverse

from labs.models import Product


class StarterProjectSmokeTest(TestCase):
    def test_login_page_can_open(self):
        response = self.client.get(reverse("login"))
        self.assertEqual(response.status_code, 200)

    def test_dashboard_and_latihan_pages_can_open(self):
        names = [
            "home",
            "css_selectors",
            "orm",
            "fetch_books",
            "debounce",
            "debug_fetch",
            "product_create",
            "table_debug",
            "events",
            "session_cookie",
            "search_flow",
        ]
        for name in names:
            with self.subTest(name=name):
                response = self.client.get(reverse(f"latihan:{name}"))
                self.assertEqual(response.status_code, 200)

    def test_books_api_returns_a_json_list(self):
        response = self.client.get(reverse("latihan:books_api"))
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)

    def test_products_api_filters_case_insensitively(self):
        Product.objects.create(name="Mouse", stock=4, price=100)
        Product.objects.create(name="Keyboard", stock=2, price=200)
        response = self.client.get(reverse("latihan:products_api"), {"q": "mou"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual([item["name"] for item in response.json()["results"]], ["Mouse"])
