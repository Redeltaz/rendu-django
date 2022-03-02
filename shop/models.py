from django.db import models

class Product(models.Model):
    price = models.IntegerField()
    image = models.CharField(max_length=255)
    description = models.CharField(max_length=510)
    quantity = models.IntegerField()