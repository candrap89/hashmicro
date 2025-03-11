from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
    name = models.CharField("name", max_length=256, unique=True, blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    barcode = models.CharField("barcode", max_length=256, unique=True, blank=False)
    stock = models.IntegerField("stock", default=0)
    inserted_at = models.DateTimeField("inserted_at", auto_now_add=True)
    updated_at = models.DateTimeField("updated_at", auto_now=True)
    updated_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True, blank=True
    )


    def __str__(self):
        return self.barcode
    
        class Meta(object):
            ordering = ['inserted_at']
            db_table = "product"
            verbose_name_plural = "products"
            permissions = [
                ("can_view_product", "Can view Proeuct"),
                ("can_add_product", "Can add Product"),
                ("can_change_product", "Can change Product"),
                ("can_delete_product", "Can delete Product"),
            ]
