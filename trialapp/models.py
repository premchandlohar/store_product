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

    def get_json(self):
        return {
            'store_id':self.id,
            'store_name':self.store_name,
            'store_location':self.store_location,
            'store_address':self.store_address,
            'store_latitude':self.store_latitude,
            'store_longitude':self.store_longitude,
            'store_city':self.store_city,
            'store_state':self.store_state
        }

        
    

class Category(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    category_name = models.CharField(max_length=30)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def get_json(self):
        return {
            'store_id':self.store.id,
            'store_name':self.store.store_name,
            'category_name':self.category_name
        }




class Subcategory(models.Model):
    store                  = models.ForeignKey(Store, on_delete=models.CASCADE)
    category               = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory_name       = models.CharField(max_length=30)

    def __str__(self):
        return self.subcategory_name

    class Meta:
        verbose_name = "Subcategory"
        verbose_name_plural = "Subcategories"

    def get_json(self):
        return {
            'store_id': self.store.id,
            'store_name': self.store.store_name,
            'category_id':self.category.id,
            'category_name': self.category.category_name,
            'subcategory_id': self.id,
            'subcategory_name':self.subcategory_name
        }




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
 
#    class instance method 

    def get_json(self):
        return {
            'store_id': self.store.id,
            'store_name': self.store.store_name,                              
            'subcategory_id': self.subcategory.id,
            'subcategory_name':self.subcategory.subcategory_name,
            'product_id': self.id,
            'product_name' : self.product_name,     
            'product_quantity' : self.product_quantity,
            'product_price' : self.product_price,       
            'product_discount_price' : self.product_discount_price,
            'product_description' : self.product_description
        }




                    


