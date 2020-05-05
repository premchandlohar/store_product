from .models import *
from django.db import transaction
from validator import *
import json

def validate_create_user(request):
    params = json.loads(request.body)
    try:
        username = params.get('username')
        password = params.get('password')
        first_name = params.get('first_name')
        last_name = params.get('last_name')
        age = params.get('age')
        email = params.get('email')

        if valid_string(username):
            return JsonResponse({'validation':'enter valid username ,must be a string'})   
        elif valid_string(password):
            return JsonResponse({'validation':'enter valid password,must be a string'})  
        elif valid_string(first_name):
            return JsonResponse({'validation':'enter valid first_name,must be a string'})   
        elif valid_string(last_name):
            return JsonResponse({'validation':'enter valid last_name,must be a string'})    
        elif valid_integer(age):
            return JsonResponse({'validation':'enter valid age,must be a integer'})
        elif valid_email(email):
            return JsonResponse({'validation':'enter valid email,must be a string'})   
        
        kwarg={
                "username":username,
                "password":password,
                "first_name":first_name,
                "last_name":last_name,
                "age":age,
                "email":email
            }

        return True, "validation successfully",kwarg

    except Exception as e:
        # print(e)
        return False, str(e), None
