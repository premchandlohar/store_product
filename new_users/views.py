
from django.contrib.auth import get_user_model
from django.db import transaction
from django.http import JsonResponse
import json
from .models import *

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
        with transaction.atomic():
            user_obj = get_user_model().objects.create(username = username)
            print(user_obj)
            user_obj.set_password(password)
            user_obj.save()

            userprofile_obj = UserProfile.objects.create(
                user = user_obj,
                first_name = first_name,
                last_name = last_name,
                age = age,
                email = email,
            )
            # userprofile_obj.save()
            # print(userprofile_obj)
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
        for user in users_obj:
            response.append(user.all_user())
        return JsonResponse({'validation':'success','response':response,'status':True})
    except Exception as e:
        return JsonResponse({'validation':str(e),'status':False})
    #       +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
def update_user_by_field(request):
    params = json.loads(request.body)

    user_id = params.get('user_id')
    username = params.get('username')
    password = params.get('password')
    first_name = params.get('first_name')
    last_name = params.get('last_name')
    age = params.get('age')
    email = params.get('email')

    try:
        with transaction.atomic():
            userprofile_obj = UserProfile.objects.get(id = user_id)
            print(userprofile_obj)
            userprofile_obj.user.username = username
            userprofile_obj.first_name = first_name
            userprofile_obj.last_name = last_name
            userprofile_obj.age = age
            userprofile_obj.email = email
            userprofile_obj.save()

            return JsonResponse({'validation':'success','status':True})
    except Exception as e:
        return JsonResponse({'validation':str(e),'status':False})

        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def create_address(request):
    params = json.loads(request.body)

    user_id = params.get('user_id')
    building_name = params.get('building_name')
    street_name = params.get('street_name')
    locality = params.get('locality')
    city = params.get('city')
    district = params.get('district')
    state = params.get('state')
    pincode = params.get('pincode')

    try:
        with transaction.atomic():
            userprofile_obj = UserProfile.objects.get(id = user_id)
            address_obj = Address.objects.create(
                userprofile = userprofile_obj,
                building_name = building_name,
                street_name = street_name,
                locality = locality,
                city = city,
                district= district,
                state = state,
                pincode = pincode
            )

            return JsonResponse({'validation':'success','status':True})
    except Exception as e:
        return JsonResponse({'validation':str(e),'status':False})
        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
def update_address_by_address_id(request):
    params = json.loads(request.body)

    user_id = params.get('user_id')
    address_id = params.get('address_id')
    building_name = params.get('building_name')
    street_name = params.get('street_name')
    locality = params.get('locality')
    city = params.get('city')
    district = params.get('district')
    state = params.get('state')
    pincode = params.get('pincode')

    try:
        with transaction.atomic():
            userprofile_obj = UserProfile.objects.get(id = user_id)
            address_obj = Address.objects.get(id=address_id)

            address_obj.userprofile = userprofile_obj
            address_obj.building_name = building_name
            address_obj.street_name = street_name
            address_obj.locality = locality
            address_obj.city = city
            address_obj.district= district
            address_obj.state = state
            address_obj.pincode = pincode
            address_obj.save()
            return JsonResponse({'validation':'success','status':True})
    except Exception as e:
        return JsonResponse({'validation':str(e),'status':False})
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def get_address_by_id(request):
    params = json.loads(request.body)
    response = []

    address_id = params.get('address_id')
    try:

        address_obj = Address.objects.get(id = address_id)
        response.append(address_obj.get_json())
        return JsonResponse({'validation':'success','response':response,'status':True})
    except Exception as e:
        return JsonResponse({'validation':str(e),'status':False})
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def get_all_address(request):
    response = []

    try:
        
        address_obj = Address.objects.all()
        for addresses in address_obj:
            response.append(addresses.get_json())
        return JsonResponse({'validation':'success','response':response,'status':True})
    except Exception as e:
        return JsonResponse({'validation':str(e),'status':False})
        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def get_addresses_of_user(request):
    params = json.loads(request.body)
    response = []

    user_id = params.get('user_id')
    # use related_name =address
    try:
        userprofile = UserProfile.objects.get(id= user_id)
        # address_qs = Address.objects.filter(userprofile=user_id )
        for address in userprofile.addresses.all():
            response.append(address.get_json())
        return JsonResponse({'validation':'success','response':response,'status':True})
    except Exception as e:
        return JsonResponse({'validation':str(e),'status':False})
        
      # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      
def delete_user_by_id(request):
    params = json.loads(request.body) 

    user_id = params.get('user_id')
    try:

        user_obj = UserProfile.objects.get(id =user_id).delete()
        return JsonResponse({'validation':'success','status':True})
    except Exception as e:
        return JsonResponse({'validation':str(e),'status':False})
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    
def delete_address_by_id(request):
    params = json.loads(request.body) 

    address_id = params.get('address_id')
    try:
        
        address_obj = Address.objects.get(id = address_id).delete()
        return JsonResponse({'validation':'success','status':True})
    except Exception as e:
        return JsonResponse({'validation':str(e),'status':False})

        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

          
           





