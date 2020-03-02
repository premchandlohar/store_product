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