from django.http import JsonResponse
from trialapp.models import *
import json
from django.db import transaction


# Create your views here.

def create_store(request):
    params = json.loads(request.body)

    store_name = params.get('store_name')
    store_location = params.get('store_location')
    store_address = params.get('store_address')
    store_latitude = params.get('store_latitude')
    store_longitude = params.get('store_longitude')
    store_city = params.get('store_city')
    store_state = params.get('store_state')

    try:
        with transaction.atomic():

            create_obj = Store.objects.create(
                store_name = store_name,
                store_location = store_location,
                store_address = store_address,
                store_latitude =  store_latitude,
                store_longitude = store_longitude,
                store_city = store_city,
                store_state = store_state
            )
            return JsonResponse({'validation':'success','status':True})
    except Exception as e:
        return JsonResponse({'validation':str(e),'status':False})
         
        #  ************************************************************************************************

def create_category(request):
    params = json.loads(request.body)
    
    category_name = params.get('category_name')
    store_id = params.get('store_id')
    print(type(store_id))

    store_obj = Store.objects.get(id= store_id)
    print(store_obj)

    try:
        with transaction.atomic():

            category_obj = Category.objects.create(
                store = store_obj,
                category_name = category_name
            )
            return JsonResponse({'validation':'success','status':True})
    except Exception as e:
        return JsonResponse({'validation':str(e),'status':False})


    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def create_subcategory(request):
    params = json.loads(request.body)

    
    store_id = params.get('store_id')
    category_id = params.get('category_id')
    subcategory_name = params.get('subcategory_name')

    store_obj = Store.objects.get(id= store_id)
    category_obj = Category.objects.get(id= category_id)

    try:
        with transaction.atomic():

            subcategory_obj = Subcategory.objects.create(
                store = store_obj,
                category = category_obj,
                subcategory_name = subcategory_name
            )
            return JsonResponse({'validation':'success','status':True})
    except Exception as e:
        return JsonResponse({'validation':str(e),'status':False})
        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def create_product(request):
    params = json.loads(request.body)

    store_id = params.get('store_id')
    subcategory_id = params.get('subcategory_id')
    product_name = params.get('product_name')
    product_quantity = params.get('product_quantity')
    product_price  = params.get('product_price')
    product_discount_price = params.get('product_discount_price')
    product_description= params.get('product_description')

    store_obj = Store.objects.get(id= store_id)
    subcategory_obj = Subcategory.objects.get(id= subcategory_id)

    try:
        with transaction.atomic():

            product_obj = Product.objects.create(
                store = store_obj,
                subcategory = subcategory_obj,
                product_name = product_name,
                product_quantity = product_quantity,
                product_price = product_price,
                product_discount_price = product_discount_price,
                product_description = product_description,
            )
            return JsonResponse({'validation':'success','status':True})
    except Exception as e:
        return JsonResponse({'validation':str(e),'status':False})

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        

def get_store_by_id(request):
    params = json.loads(request.body)

    response=[]
    store_id = params.get('store_id')

    try:
        # with transaction.atomic():

        store_obj = Store.objects.get(id=store_id)
        response.append ({
            'store_id':store_obj.id,
            'store_name':store_obj.store_name,
            'store_location':store_obj.store_location,
            'store_address':store_obj.store_address,
            'store_latitude':store_obj.store_latitude,
            'store_longitude':store_obj.store_longitude,
            'store_location':store_obj.store_location,
            'store_city':store_obj.store_city,
            'store_state':store_obj.store_state
        })
        return JsonResponse({'validation':'success','respinse':response,'status':True})
    except Exception as e:
        return JsonResponse({'validation':str(e),'status':False})

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def get_category_by_id(request):
    params = json.loads(request.body)

    response = []
    category_id = params.get('category_id')

    try:

        category_obj = Category.objects.get(id=category_id)
        print(category_obj)
        response.append({
            'store_id':category_obj.store.id,
            'store_name':category_obj.store.store_name,
            'category_name':category_obj.category_name
        })
        return JsonResponse({'validation':'success','respinse':response,'status':True})
    except Exception as e:
        return JsonResponse({'validation':str(e),'status':False})
    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def get_subcategory_by_id(request):
    params = json.loads(request.body)

    response = []
    subcategory_id = params.get('subcategory_id')

    try:
        
        subcategory_obj = Subcategory.objects.get(id=subcategory_id)
        response.append({
            'store_id': subcategory_obj.store.id,
            'store_name': subcategory_obj.store.store_name,
            'category_id':subcategory_obj.category.id,
            'category_name': subcategory_obj.category.category_name,
            'subcategory_id': subcategory_obj.id,
            'subcategory_name':subcategory_obj.subcategory_name
        })
        return JsonResponse({'validation':'success','respinse':response,'status':True})
    except Exception as e:
        return JsonResponse({'validation':str(e),'status':False})

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def get_product_by_id(request):
    params = json.loads(request.body)

    response = []
    product_id = params.get('product_id')

    try:
        
        product_obj = Product.objects.get(id=product_id)
        response.append({
            'store_id': product_obj.store.id,
            'store_name': product_obj.store.store_name,
            'subcategory_id': product_obj.subcategory.id,
            'subcategory_name':product_obj.subcategory.subcategory_name,
            'product_name' :  product_obj.product_name,     
            'product_quantity' :  product_obj.product_quantity,
            'product_price' :  product_obj.product_price,       
            'product_discount_price' :  product_obj.product_discount_price,
            'product_description' :  product_obj.product_description
        })
        return JsonResponse({'validation':'success','respinse':response,'status':True})
    except Exception as e:
        return JsonResponse({'validation':str(e),'status':False})
        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def get_all_store(request):
    response=[]

    try:

        all_store = Store.objects.all()
        for store in all_store:
            response.append({
                'store_id':store.id,
                'store_name':store.store_name,
                'store_location':store.store_location,
                'store_address':store.store_address,
                'store_latitude':store.store_latitude,
                'store_longitude':store.store_longitude,
                'store_location':store.store_location,
                'store_city':store.store_city,
                'store_state':store.store_state 
            })
        return JsonResponse({'validation':'success','response':response,'status':True})
    except Exception as e:
        return JsonResponse({'validation':str(e),'status':False})
        
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def get_all_category(request):
    response = []

    try:

        category_obj = Category.objects.all()
        for category in category_obj:
            response.append({
                'store_id':category.store.id,
                'store_name':category.store.store_name,
                'category_id':category.id,
                'category_name':category.category_name
            })
        return JsonResponse({'validation':'success','respinse':response,'status':True})
    except Exception as e:
        return JsonResponse({'validation':str(e),'status':False})
    
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def get_all_subcategory(request):
    response = []

    try:

        subcategory_obj = Subcategory.objects.all()
        for subcategory in subcategory_obj:
            response.append({
                'store_id':subcategory.store.id,
                'store_name':subcategory.store.store_name,
                'subcategory_id':subcategory.id,
                'subcategory_name':subcategory.subcategory_name
            })
        return JsonResponse({'validation':'success','respinse':response,'status':True})
    except Exception as e:
        return JsonResponse({'validation':str(e),'status':False})
    


        



        



                










       

#         #  **************************************************************************************************************

# def get_product_by_id(request):
#     response=[]
#     params = json.loads(request.body)
#     product_id = params.get('product_id')
#     try:
#         create_obj = Product.objects.get(id=product_id)
#         response.append ({
#             'store_name':create_obj.store.store_name,
#             'product_id':create_obj.id,
#             'product_name':create_obj.product_name,
#             'product_quantity':create_obj.product_quantity,
#             'product_price':create_obj.product_price
#         })
#         return JsonResponse({'validation':'success','response':response,'status':True})
    
#     except Exception as e:
#         return JsonResponse({'validation':str(e),'status':False})

#         # *****************************************************************************************************
# def get_all_store(request):
#     response=[]
#     try:
#         all_store = Store.objects.all()
#         for store in all_store:
#             response.append({
#                 'store_id':store.id,
#                 'store_name':store.store_name,
#                 'store_location':store.store_location,
#                 'store_city':store.store_city,
#                 'store_state':store.store_state 
#             })
#         return JsonResponse({'validation':'success','response':response,'status':True})
        
#     except Exception as e:
#         return JsonResponse({'validation':str(e),'status':False})

#         # ***************************************************************************************************************
# def get_all_product(request):
#     response=[]
#     try:
#         all_product = Product.objects.all()
#         print(all_product)
#         for product in all_product:
#             response.append({
#                 'product_id':product.id,
#                 'product_store':product.store.store_name,
#                 'product_name':product.product_name,
#                 'product_quantity':product.product_quantity,
#                 'product_price':product.product_price
#             })
#         return JsonResponse({'validation':'success','response':response,'status':True})
        
#     except Exception as e:
#         return JsonResponse({'validation':str(e),'status':False})

#         # ********************************************************************************************************
# def get_products_by_store_id(request):
#     response = []
#     params = json.loads(request.body)
#     store_id = params.get('store_id')
#     store = Store.objects.get(id=store_id)
#     product_qs =Product.objects.filter(store=store)
#     print(product_qs)
#     for obj in product_qs:
#         response.append({
#                 'product_id':obj.id,
#                 'product_store':obj.store.store_name,
#                 'product_name':obj.product_name,
#                 'product_quantity':obj.product_quantity,
#                 'product_price':obj.product_price
#         })
#     return JsonResponse({'validation':'success','response':response,'status':True})

# # ******************************************************************************************************************
# def delete_store_by_id(reqsuest):
#     params = json.loads(reqsuest.body)
#     store_id = params.get('store_id')
#     create_obj = Store.objects.get(id=store_id).delete()
#     return JsonResponse({'validation':'success','status':True})
         
# # ******************************************************************************************************************
# def delete_product_by_id(reqsuest):
#     params = json.loads(reqsuest.body)
#     product_id = params.get('product_id')
#     delete_obj = Product.objects.get(id=product_id).delete()
#     return JsonResponse({'validation':'success','status':True})

#     # ***********************************************************************************************************
# def update_store_by_id(request):
#     # response =[]
#     params = json.loads(request.body)
#     store_id = params.get('store_id')
#     store_name = params.get('store_name')
#     store_location = params.get('store_location')
#     store_city = params.get('store_city')
#     store_state = params.get('store_state')
#     update_obj = Store.objects.filter(id = store_id).update(store_name = store_name,
#         store_location = store_location,store_city = store_city,store_state = store_state
#         )
    
#     # update_obj = Store.objects.filter(id = store_id).update(**params)
#     # for obj in update_obj:
#     #     response.append({
#     #         'store_name': obj.store_name,
#     #         'store_location':obj.store_location,
#     #         'store_city':obj.store_city,
#     #         'store_state':obj.store_state
#     #     })
#     return JsonResponse({'validation':'success','status':True})

#     # return JsonResponse({'validation':'success','response':response,'status':True})

#     # *************************************************************************************************************
# def update_product_by_id(request):
#     params = json.loads(request.body)
#     product_id = params.get('product_id') 
#     store = params.get('store') 
#     product_name = params.get('product_name')    
#     product_quantity = params.get('product_quantity') 
#     product_price = params.get('product_price') 
#     obj = Store.objects.get(id=store)
#     update_product = Product.objects.filter(id = product_id).update(store = obj,
#         product_name = product_name, product_quantity = product_quantity, product_price = product_price
#         )
#     # update_product = Product.objects.filter(id = product_id).update(**params)
#     return JsonResponse({'validation':'success','status':True})     
    
# # **************************************************************************************************************
# def update_product_by_store_id(request):
#     params = json.loads(request.body)
#     # store_id = params.get('store_id')
#     store = params.get('store') 
#     product_name = params.get('product_name')    
#     product_quantity = params.get('product_quantity') 
#     product_price = params.get('product_price')
#     store_obj = Store.objects.get(id=store)
#     product_obj = Product.objects.filter(store = store_obj)
#     update_product = Product.objects.filter(id =15).update(store = store,
#         product_name = product_name, product_quantity = product_quantity, product_price = product_price
#         )
#     return JsonResponse({'validation':'success','status':True}) 

# # ****************************************************************************************************************
# def update_store_by_field(request):
#     params = json.loads(request.body)
#     store_id = params.get('store_id')
#     store_name = params.get('store_name')
#     store_location = params.get('store_location')
#     store_city = params.get('store_city')
#     store_state = params.get('store_state')
#     # Store.store_name =  store_name  
#     obj = Store.objects.get(id = store_id)
#     # for obj in object:
#     obj.store_name = store_name
#     obj.store_location = store_location
#     obj.store_city = store_city
#     obj.store_state = store_state
#     obj.save()

#     return JsonResponse({'validation':'success','status':True}) 

#     # *************************************************************************************************************8
# def update_product_by_field(request):
#     params = json.loads(request.body)
#     product_id = params.get('product_id')
#     store = params.get('store')
#     product_name = params.get('product_name')
#     product_quantity = params.get('product_quantity')
#     product_price = params.get('product_price')
#     store_obj = Store.objects.get(id=store)
#     obj  = Product.objects.get(id = product_id)

#     obj.store = store_obj
#     obj.product_name =  product_name
#     obj.product_quantity = product_quantity
#     obj.product_price = product_price
#     obj.save()
#     return JsonResponse({'validation':'success','status':True})
    
# # *****************************************************************************************************8
# def update_or_create_store_by_id(request):
#     params = json.loads(request.body)
#     store_id = params.get('store_id')
#     store_name = params.get('store_name')
#     store_location = params.get('store_location')
#     store_city = params.get('store_city')
#     store_state = params.get('store_state')
#     update,status = Store.objects.update_or_create( id= store_id,
        
#                 defaults = {'store_name':store_name,
#                 "store_city": store_city,
#                 "store_state" : store_state,
#                 "store_location" : store_location
#                 }
#             )
#     print("status",status)
#     return JsonResponse({'validation':'success','status':True}) 

# #     # *************************************************************************************************************
# def update_or_create_product_by_id(request):
#     response = []
#     params = json.loads(request.body)
#     product_id = params.get('product_id')
#     store_id = params.get('store_id')
#     product_name = params.get('product_name')
#     product_quantity = params.get('product_quantity')
#     product_price = params.get('product_price')
#     store_obj = Store.objects.get(id=store_id)
#     update,status  = Product.objects.update_or_create(id = product_id, defaults = {
#         # 'store_name':store_obj.store_name,
#         'product_name':product_name,'product_quantity':product_quantity,'product_price':product_price,
#         'store_id':store_id 
#         })
#     response.append({
#         'store_name':store_obj.store_name,
#         'product_name':product_name,'product_quantity':product_quantity
#         })
#     print("status",status)
#     return JsonResponse({'validation':'success','response':response,'status':True})
#     # **************************************************************************************************************
# def get_or_create_store_by_id(request):
#     with transaction.atomic():
#         response =[]
#         params = json.loads(request.body)
#         store_id = params.get('store_id')
#         store_name = params.get('store_name')
#         store_location = params.get('store_location')
#         store_city = params.get('store_city')
#         store_state = params.get('store_state')
#         get,status = Store.objects.get_or_create( id= store_id,
#                     defaults = {'store_name':store_name,
#                     'store_location' : store_location,
#                     'store_city': store_city,
#                     'store_state' : store_state,
#                 })
            
#         response.append ({
#             'store_id':store_id,
#             'store_name':store_name,
#             'store_location':store_location,
#             'store_city':store_city,
#             'store_state':store_state
#             })
#         print("status",status)
#     return JsonResponse({'validation':'success','response':response,'status':True})

# # ****************************************************************************************************************
# def get_or_create_product_by_id(request):
#     response = []
#     params = json.loads(request.body)
#     product_id = params.get('product_id')
#     store_id = params.get('store_id')
#     product_name = params.get('product_name')
#     product_quantity = params.get('product_quantity')
#     product_price = params.get('product_price')
#     store_obj = Store.objects.get(id=store_id)
#     update,status  = Product.objects.get_or_create(id = product_id, defaults = {
#         # 'store_name':store_obj.store_name,
#         'product_name':product_name,'product_quantity':product_quantity,'product_price':product_price,
#         'store_id':store_id 
#         })
#     response.append({
#         'store_name':store_obj.store_name,'product_id':product_id,
#         'product_name':product_name,'product_quantity':product_quantity,'product_price':product_price
#         })
#     print("status",status)
#     return JsonResponse({'validation':'success','response':response,'status':True})

# # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++











    
