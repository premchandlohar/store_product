from django.db import models
from django.contrib.auth import get_user_model
from datetime import datetime
# from trialapp.models import Store,Followership  


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(get_user_model(),on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.PositiveSmallIntegerField()
    email = models.EmailField(max_length=255,unique=False)
    created_on = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    # following= models.ManyToManyField(Store, through = 'Followership',related_name='following',
    # blank =True)

    def __str__(self):
        return self.first_name + " " + self.last_name

    def get_json(self):
        return {
            "username": self.user.username,
            "first_name" : self.first_name,
            "last_name" : self.last_name,
            "age" : self.age,
            "email" : self.email,
            "created_on" :self.created_on
        }

    def all_user(self):
        return {
            "user_id" : self.id,
            "username": self.user.username,
            "first_name" : self.first_name,
            "last_name" : self.last_name,
            "age" : self.age,
            "email" : self.email,
            "created_on" :self.created_on
        }

    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class Address(models.Model):
    userprofile = models.ForeignKey(UserProfile,on_delete=models.CASCADE,related_name='addresses')
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
        verbose_name = "Address"
        verbose_name_plural = "Addresses"

    def get_json(self):
        return {
            "user_id" : self.userprofile.id,
            "first_name" : self.userprofile.first_name,
            "last_name" : self.userprofile.last_name,
            "building_name" : self.building_name,
            "street_name" : self.street_name,
            "locality" : self.locality,
            "city" : self.city,
            "district" : self.district,
            "state" : self.state,
            "pincode" : self.pincode
        }

        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++






            
