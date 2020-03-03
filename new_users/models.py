from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model




# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(get_user_model(),on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.PositiveSmallIntegerField()
    email = models.EmailField(max_length=255,unique=True)

    def __str__(self):
        return self.first_name + " " + self.last_name

    def get_json(self):
        return {
            "username": self.user.username,
            "first_name" : self.first_name,
            "last_name" : self.last_name,
            "age" : self.age,
            "email" : self.email
        }

    def all_user(self):
        return {
            "user_id" : self.id,
            "username": self.user.username,
            "first_name" : self.first_name,
            "last_name" : self.last_name,
            "age" : self.age,
            "email" : self.email
        }
    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class Address(models.Model):
    userprofile = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    building_name =  models.CharField(max_length=30)
    street_name =  models.CharField(max_length=30)
    locality =  models.CharField(max_length=30)
    city =  models.CharField(max_length=30)
    district =  models.CharField(max_length=30)
    state =  models.CharField(max_length=30)
    pincode =  models.DecimalField(max_digits = 10,decimal_places = 4)

    def __str__(self):
        return self.userprofile.first_name +" "+ self.userprofile.last_name

    class Meta:
        # verbose_name = "Category"
        verbose_name_plural = "Addresses"