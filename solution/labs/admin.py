from django.contrib import admin

from .models import Document, Product


admin.site.register(Product)
admin.site.register(Document)

