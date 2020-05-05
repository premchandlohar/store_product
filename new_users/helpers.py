from .models import *
from django.db import transaction
from django.core.exceptions import ObjectDoesNotExist
# from new_users.models import *
from django.contrib.auth import get_user_model


def create_user_function(data):
    try:
        with transaction.atomic():
            user_obj = get_user_model().objects.create(username = data['username'])
#             print(user_obj)
            user_obj.set_password(data['password'])
            user_obj.save()

            userprofile_obj = UserProfile.objects.create(
                user = user_obj,
                first_name = data['first_name'],
                last_name =data['last_name'],
                age = data['age'],
                email = data['email'],
            )
        return {'user data':userprofile_obj},True
    except Exception as e:
        return None,False