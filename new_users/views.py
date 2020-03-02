# from django.shortcuts import render
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

from django.http import JsonResponse
import json
from .models import UserProfile

# Create your views here.
def create_user(request):
    params = json.loads(request.body)

    username = params.get('username')
    password = params.get('password')
    first_name = params.get('first_name')
    last_name = params.get('last_name')
    age = params.get('age')
    email = params.get('email')

    try:
        user_obj = get_user_model().objects.create_user(
            username = username,
            password = password
        )


        userprofile_obj = UserProfile.objects.create(
            user = user_obj,
            first_name = first_name,
            last_name = last_name,
            age = age,
            email = email
        )
        return JsonResponse({'validation':'success','status':True})
    except Exception as e:
        return JsonResponse({'validation':str(e),'status':False})
        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def get_user_by_id(request):
    response =[]
    params = json.loads(request.body)

    user_id = params.get('user_id')

    try:

        get_user_obj = UserProfile.objects.get(id= user_id)
        # print(get_user_obj)
        response.append(get_user_obj.get_json())
        print(response)
        return JsonResponse({'validation':'success','response':response,'status':True})
    except Exception as e:
        return JsonResponse({'validation':str(e),'status':False})
    
def get_all_users(request):
    response =[]

    try:
        users_obj = UserProfile.objects.all()
        for users in users_obj:
            response.append(users.all_user())
        return JsonResponse({'validation':'success','response':response,'status':True})
    except Exception as e:
        return JsonResponse({'validation':str(e),'status':False})
    


