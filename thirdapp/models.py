from django.db import models
from datetime import datetime,date

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length = 30)

    def __str__(self):
        return self.name

    def get_json(self):
        return {
            "name" : self.name
        }

    # **************************************************************************************************

class Group(models.Model):
    name = models.CharField(max_length = 30)
    members = models.ManyToManyField(Person, through = 'Membership') 

    def __str__(self):
        return self.name
    
    def get_json(self):
        return {
            "name" : self.name,
            # "members" : self.members
        }


    # **************************************************************************************************

class Membership(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE,related_name='information')
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined = models.DateField(auto_now_add=True,null=True,blank=True)
    invite_reason = models.CharField(max_length=64)

    def get_json(self):
        return {
            "person" : self.person.name,
            "group": self.group.name,
            "invite_reason" : self.invite_reason,
            "date_joined" : self.date_joined
        }

