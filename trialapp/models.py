from django.db import models

# Create your models here.
class Store(models.Model):
    store_name = models.CharField(max_length=30)
    store_location = models.CharField(max_length=30)
    store_address  = models.CharField(max_length=60)
    store_latitude = models.DecimalField( max_digits=6, decimal_places=2)
    store_longitude= models.DecimalField( max_digits=6, decimal_places=2)
    store_city = models.CharField(max_length=30)
    store_state = models.CharField(max_length=30)

    def __str__(self):
        return self.store_name

class Category(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    category_name = models.CharField(max_length=30)


class Subcategory(models.Model):
     store                  = models.ForeignKey(Store, on_delete=models.CASCADE)
     category               = models.ForeignKey(Category, on_delete=models.CASCADE)
     subcategory_name       = models.CharField(max_length=30)

class Product(models.Model):
    store                  = models.ForeignKey(Store, on_delete=models.CASCADE)
    subcategory            = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    product_name           = models.CharField(max_length=30)
    product_quantity       = models.DecimalField( max_digits=6, decimal_places=2)
    product_price          = models.FloatField()
    product_discount_price = models.FloatField()
    product_description    = models.TextField(max_length=801)
    
    def __str__(self):
        return self.product_name




                    


