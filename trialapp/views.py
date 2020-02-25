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
         
# ******************************************************************************************************************
def delete_product_by_id(reqsuest):
    params = json.loads(reqsuest.body)
    product_id = params.get('product_id')
    delete_obj = Product.objects.get(id=product_id).delete()
    return JsonResponse({'validation':'success','status':True})

    # ***********************************************************************************************************
def update_store_by_id(request):
    # response =[]
    params = json.loads(request.body)
    store_id = params.get('store_id')
    store_name = params.get('store_name')
    store_location = params.get('store_location')
    store_city = params.get('store_city')
    store_state = params.get('store_state')
    update_obj = Store.objects.filter(id = store_id).update(store_name = store_name,
        store_location = store_location,store_city = store_city,store_state = store_state
        )
    
    # update_obj = Store.objects.filter(id = store_id).update(**params)
    # for obj in update_obj:
    #     response.append({
    #         'store_name': obj.store_name,
    #         'store_location':obj.store_location,
    #         'store_city':obj.store_city,
    #         'store_state':obj.store_state
    #     })
    return JsonResponse({'validation':'success','status':True})

    # return JsonResponse({'validation':'success','response':response,'status':True})

    # *************************************************************************************************************
def update_product_by_id(request):
    params = json.loads(request.body)
    product_id = params.get('product_id') 
    store = params.get('store') 
    product_name = params.get('product_name')    
    product_quantity = params.get('product_quantity') 
    product_price = params.get('product_price') 
    obj = Store.objects.get(id=store)
    update_product = Product.objects.filter(id = product_id).update(store = obj,
        product_name = product_name, product_quantity = product_quantity, product_price = product_price
        )
    # update_product = Product.objects.filter(id = product_id).update(**params)
    return JsonResponse({'validation':'success','status':True})     
    
# **************************************************************************************************************
def update_product_by_store_id(request):
    params = json.loads(request.body)
    # store_id = params.get('store_id')
    store = params.get('store') 
    product_name = params.get('product_name')    
    product_quantity = params.get('product_quantity') 
    product_price = params.get('product_price')
    store_obj = Store.objects.get(id=store)
    product_obj = Product.objects.filter(store = store_obj)
    update_product = Product.objects.filter(id =15).update(store = store,
        product_name = product_name, product_quantity = product_quantity, product_price = product_price
        )
    return JsonResponse({'validation':'success','status':True}) 

# ****************************************************************************************************************
def update_store_by_field(request):
    params = json.loads(request.body)
    store_id = params.get('store_id')
    store_name = params.get('store_name')
    store_location = params.get('store_location')
    store_city = params.get('store_city')
    store_state = params.get('store_state')
    # Store.store_name =  store_name  
    obj = Store.objects.get(id = store_id)
    # for obj in object:
    obj.store_name = store_name
    obj.store_location = store_location
    obj.store_city = store_city
    obj.store_state = store_state
    obj.save()

    return JsonResponse({'validation':'success','status':True}) 

    # *************************************************************************************************************8
def update_product_by_field(request):
    params = json.loads(request.body)
    product_id = params.get('product_id')
    store = params.get('store')
    product_name = params.get('product_name')
    product_quantity = params.get('product_quantity')
    product_price = params.get('product_price')
    store_obj = Store.objects.get(id=store)
    obj  = Product.objects.filter(id = product_id)

    obj.store = store_obj
    obj.product_name =  product_name
    obj.product_quantity = product_quantity
    obj.product_price = product_price
    obj.save()
    return JsonResponse({'validation':'success','status':True})
    
# *****************************************************************************************************8
def update_or_create_store_by_id(request):
    params = json.loads(request.body)
    store_id = params.get('store_id')
    store_name = params.get('store_name')
    store_location = params.get('store_location')
    store_city = params.get('store_city')
    store_state = params.get('store_state')
    update,status = Store.objects.update_or_create( id= store_id,
        
                defaults = {'store_name':store_name,
                "store_city": store_city,
                "store_state" : store_state,
                "store_location" : store_location
                }
            )
    print("status",status)
    return JsonResponse({'validation':'success','status':True}) 

#     # *************************************************************************************************************
def update_or_create_product_by_id(request):
    response = []
    params = json.loads(request.body)
    product_id = params.get('product_id')
    store_id = params.get('store_id')
    product_name = params.get('product_name')
    product_quantity = params.get('product_quantity')
    product_price = params.get('product_price')
    store_obj = Store.objects.get(id=store_id)
    update,status  = Product.objects.get_or_create(id = product_id, defaults = {
        # 'store_name':store_obj.store_name,
        'product_name':product_name,'product_quantity':product_quantity,'product_price':product_price,
        'store_id':store_id 
        })
    response.append({
        'store_name':store_obj.store_name,
        'product_name':product_name,'product_quantity':product_quantity
        })
    print("status",status)
    return JsonResponse({'validation':'success','response':response,'status':True})
    # **************************************************************************************************************
def get_or_create_store_by_id(request):
    with transaction.atomic():
        response =[]
        params = json.loads(request.body)
        store_id = params.get('store_id')
        store_name = params.get('store_name')
        store_location = params.get('store_location')
        store_city = params.get('store_city')
        store_state = params.get('store_state')
        get,status = Store.objects.get_or_create( id= store_id,
                    defaults = {'store_name':store_name,
                    'store_location' : store_location,
                    'store_city': store_city,
                    'store_state' : store_state,
                })
            
        response.append ({
            'store_id':store_id,
            'store_name':store_name,
            'store_location':store_location,
            'store_city':store_city,
            'store_state':store_state
            })
        print("status",status)
    return JsonResponse({'validation':'success','response':response,'status':True})

# ****************************************************************************************************************











    
