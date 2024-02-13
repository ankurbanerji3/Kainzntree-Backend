from django.db import models
from django.conf import settings

# Create your models here.

class Product(models.Model):
    # user_email = models.EmailField()
    # name = models.CharField(max_length=255, null=False, blank=False)
    # category = models.CharField(max_length=255, null=False, blank=False)
    # price = models.DecimalField(max_digits=6, decimal_places=2)
    # description = models.TextField(max_length=1000)
    # stars = models.IntegerField()

    # def __str__(self):
    #     return self.name

    user_email = models.EmailField()
    SKU = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=100)
    tags = models.CharField(max_length=100, blank=True)
    category = models.CharField(max_length=100)
    in_stock = models.BooleanField(default=True)
    available_stock = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.SKU} - {self.name}"