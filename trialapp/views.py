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
def create_product(request):
    params = json.loads(request.body)
    store = params.get('store')
    product_name = params.get('product_name')
    product_quantity = params.get('product_quantity')
    product_price = params.get('product_price')
    try:
        obj = Store.objects.get(id=store)
        create_obj = Product.objects.create(
            store = obj,
            product_name =    product_name,
            product_quantity = product_quantity,
            product_price = product_price
        )
        return JsonResponse({'validation':'success','status':True})
        
    except Exception as e:
        return JsonResponse({'validation':str(e),'status':False})

  #  **************************************************************************************************************

def get_store_by_id(request):
    response=[]
    params = json.loads(request.body)
    store_id = params.get('store_id')
    try:
        create_obj = Store.objects.get(id=store_id)
        response.append ({
            'store_id':create_obj.id,
            'store_name':create_obj.store_name,
            'store_location':create_obj.store_location,
            'store_city':create_obj.store_city,
            'store_state':create_obj.store_state
        })
        return JsonResponse({'validation':'success','respinse':response,'status':True})
    
    except Exception as e:
        return JsonResponse({'validation':str(e),'status':False})

        #  **************************************************************************************************************

def get_product_by_id(request):
    response=[]
    params = json.loads(request.body)
    product_id = params.get('product_id')
    try:
        create_obj = Product.objects.get(id=product_id)
        response.append ({
            'store_name':create_obj.store.store_name,
            'product_id':create_obj.id,
            'product_name':create_obj.product_name,
            'product_quantity':create_obj.product_quantity,
            'product_price':create_obj.product_price
        })
        return JsonResponse({'validation':'success','response':response,'status':True})
    
    except Exception as e:
        return JsonResponse({'validation':str(e),'status':False})

        # *****************************************************************************************************
def get_all_store(request):
    response=[]
    try:
        all_store = Store.objects.all()
        for store in all_store:
            response.append({
                'store_id':store.id,
                'store_name':store.store_name,
                'store_location':store.store_location,
                'store_city':store.store_city,
                'store_state':store.store_state 
            })
        return JsonResponse({'validation':'success','response':response,'status':True})
        
    except Exception as e:
        return JsonResponse({'validation':str(e),'status':False})

        # ***************************************************************************************************************
def get_all_product(request):
    response=[]
    try:
        all_product = Product.objects.all()
        print(all_product)
        for product in all_product:
            response.append({
                'product_id':product.id,
                'product_store':product.store.store_name,
                'product_name':product.product_name,
                'product_quantity':product.product_quantity,
                'product_price':product.product_price
            })
        return JsonResponse({'validation':'success','response':response,'status':True})
        
    except Exception as e:
        return JsonResponse({'validation':str(e),'status':False})

        # ********************************************************************************************************
def get_products_by_store_id(request):
    response = []
    params = json.loads(request.body)
    store_id = params.get('store_id')
    store = Store.objects.get(id=store_id)
    product_qs =Product.objects.filter(store=store)
    print(product_qs)
    for obj in product_qs:
        response.append({
                'product_id':obj.id,
                'product_store':obj.store.store_name,
                'product_name':obj.product_name,
                'product_quantity':obj.product_quantity,
                'product_price':obj.product_price
        })
    return JsonResponse({'validation':'success','response':response,'status':True})

# ******************************************************************************************************************
def delete_store_by_id(reqsuest):
    params = json.loads(reqsuest.body)
    store_id = params.get('store_id')
    create_obj = Store.objects.get(id=store_id).delete()
    return JsonResponse({'validation':'success','status':True})
#          
# ******************************************************************************************************************










    
