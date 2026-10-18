from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from labs.models import Document


class DocumentAuthorizationLatihanTest(TestCase):
    def setUp(self):
        user_model = get_user_model()
        self.alice = user_model.objects.create_user("alice")
        self.bob = user_model.objects.create_user("bob")
        self.alice_document = Document.objects.create(
            owner=self.alice,
            title="Alice Document",
            content="Alice only",
        )
        self.bob_document = Document.objects.create(
            owner=self.bob,
            title="Bob Document",
            content="Bob only",
        )

    def test_owner_can_open_own_document(self):
        response = self.client.get(
            reverse("latihan:document_detail", args=[self.alice_document.id]),
            {"as_user": "alice"},
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Alice Document")

    def test_other_users_document_is_not_exposed(self):
        response = self.client.get(
            reverse("latihan:document_detail", args=[self.bob_document.id]),
            {"as_user": "alice"},
        )
        self.assertEqual(response.status_code, 404)
