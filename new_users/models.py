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
        return self.user.username

    def get_json(self):
        return {
            "first_name" : self.first_name,
            "last_name" : self.last_name,
            "email" : self.email
        }

    def all_user(self):
        return {
            "username": self.user.username,
            "email" : self.email

        }
    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class 