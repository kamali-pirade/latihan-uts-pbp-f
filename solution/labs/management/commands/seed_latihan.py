from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

from labs.models import Document, Product


class Command(BaseCommand):
    help = "Membuat data contoh idempoten untuk seluruh latihan PBP."

    def handle(self, *args, **options):
        user_model = get_user_model()

        alice, _ = user_model.objects.get_or_create(username="alice")
        alice.set_password("latihan123")
        alice.save()

        bob, _ = user_model.objects.get_or_create(username="bob")
        bob.set_password("latihan123")
        bob.save()

        samples = [
            ("Buku Django", 8, 125000),
            ("Keyboard", 0, 450000),
            ("Mouse", 15, 175000),
            ("Webcam", 3, 550000),
        ]
        for name, stock, price in samples:
            Product.objects.update_or_create(
                name=name,
                defaults={"stock": stock, "price": price},
            )

        Document.objects.update_or_create(
            owner=alice,
            title="Catatan Alice",
            defaults={"content": "Dokumen ini hanya boleh dibaca Alice."},
        )
        Document.objects.update_or_create(
            owner=bob,
            title="Catatan Bob",
            defaults={"content": "Dokumen ini hanya boleh dibaca Bob."},
        )

        self.stdout.write(self.style.SUCCESS("Data latihan siap."))
        self.stdout.write("Login Latihan 09: alice / latihan123 atau bob / latihan123")
