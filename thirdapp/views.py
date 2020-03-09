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
    # member = params.get('member')

    try:
        with transaction.atomic():
            group_obj = Group.objects.create(
                name = name
                # member = member
            )
            return JsonResponse({'validation':'success','status':True})
    except Exception as e:
        return JsonResponse({'validation':str(e), 'status':False})

    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++        
