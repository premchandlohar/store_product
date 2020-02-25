from django.db import models

# Create your models here.
class Store(models.Model):
    store_name    =models.CharField(max_length=30)
    store_location=models.CharField(max_length=30)
    store_city    =models.CharField(max_length=30)
    store_state   =models.CharField(max_length=30)

    def __str__(self):
        return self.store_name


class Product(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    product_name     = models.CharField(max_length=30)
    product_quantity = models.IntegerField()
    product_price    = models.FloatField()

# class Person(models.Model):
#     name = models.CharField(max_length=30)

    def __str__(self):
        return self.product_name
