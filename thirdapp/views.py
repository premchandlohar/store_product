from django.db import transaction
from django.http import JsonResponse
import json
from .models import *


# Create your views here.
def create_person(request):
    params = json.loads(request.body)

    name = params.get('name')

    try:
        with transaction.atomic():
            person_obj = Person.objects.create(
                name = name
            )
            return JsonResponse({'validation':'success','status':True})
    except Exception as e:
        return JsonResponse({'validation':str(e), 'status':False})

    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++        
def create_group(request):
    params = json.loads(request.body)

    name = params.get('name')

    try:
        with transaction.atomic():
            group_obj = Group.objects.create(
                name = name
            )
            return JsonResponse({'validation':'success','status':True})
    except Exception as e:
        return JsonResponse({'validation':str(e), 'status':False})

    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++        

def get_person(request):
    params = json.loads(request.body)
    response = []

    person_id = params.get('person_id')

    try:
        person_obj = Person.objects.get(id = person_id)
        response.append(person_obj.get_json())
            
        return JsonResponse({'validation':'success','response':response,'status':True})
    except Exception as e:
        return JsonResponse({'validation':str(e), 'status':False})

    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++        

def get_group(request):
    params = json.loads(request.body)
    response = []

    group_id = params.get('group_id')

    try:
        group_obj = Group.objects.get(id = group_id)
        response.append(group_obj.get_json())
            
        return JsonResponse({'validation':'success','response':response,'status':True})
    except Exception as e:
        return JsonResponse({'validation':str(e), 'status':False})

    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++        

def create_membership(request):
    params = json.loads(request.body)

    person_id = params.get('person_id')
    group_id = params.get('group_id')
    invite_reason = params.get('invite_reason')

    try:
        with transaction.atomic():
            person_obj = Person.objects.get(id=person_id)
            group_obj = Group.objects.get(id=group_id)

            membersh_obj = Membership.objects.create(
                person = person_obj, 
                group = group_obj,
                invite_reason = invite_reason  
                )
            return JsonResponse({'validation':'success','status':True})
    except Exception as e:
        return JsonResponse({'validation':str(e), 'status':False})


    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++    
        
def get_membership(request):
    params = json.loads(request.body)
    response = []

    membership_id = params.get('membership_id')
    try:
        membership_obj = Membership.objects.get(id = membership_id)
        response.append(membership_obj.get_json())
        return JsonResponse({'validation':'success','response':response,'status':True})
    except Exception as e:
        return JsonResponse({'validation':str(e), 'status':False})

        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++



