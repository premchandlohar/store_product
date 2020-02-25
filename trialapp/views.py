from django.http import JsonResponse
from trialapp.models import *
import json
from django.db import transaction


# Create your views here.

def create_store(request):
    params = json.loads(request.body)
    store_name = params.get('store_name')
    store_location = params.get('store_location')
    store_city = params.get('store_city')
    store_state = params.get('store_state')
    try:
        create_obj = Store.objects.create(
            store_name = store_name,
            store_location = store_location,
            store_city = store_city,
            store_state = store_state
        )
        return JsonResponse({'validation':'success','status':True})
    
    except Exception as e:
        return JsonResponse({'validation':str(e),'status':False})
         
        #  ************************************************************************************************







    
