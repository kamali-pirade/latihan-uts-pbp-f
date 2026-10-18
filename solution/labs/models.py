from django.conf import settings
from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=120)
    stock = models.PositiveIntegerField(default=0)
    price = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Document(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="latihan_documents",
    )
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.title

