from django.http import JsonResponse
from trialapp.models import *
import json
from django.db import transaction
from validator import *
from .validations import *
from .helpers import *


# Create your views here.
def create_store(request):
    status, message, data = validate_create_store(request)
    print( status, message, data)
    # print(status)
    if status==False:
        return JsonResponse({"validation": message, "status": status })
    # else:
        # return JsonResponse({"validation": message, "status": status })

    store_data, status = create_store_function(data)
    # print(store_data)
    if  status:
        # print(status)
        return JsonResponse({"validation message" : "successful", "status" : status })
    else:
        return JsonResponse({"validation message" : "unsuccessful", "status" :status })
    # params = request.POST

    # store_name = params.get('store_name')
    # store_location = params.get('store_location')
    # store_address = params.get('store_address')
    # store_latitude = float(params.get('store_latitude'))
    # store_longitude = float(params.get('store_longitude'))
    # store_city = params.get('store_city')
    # store_state = params.get('store_state')
    # store_image = request.FILES.get('store_image')

    # if valid_string(store_name):
    #     return JsonResponse({'validation':'enter valid store name,must be a string'})
    # elif valid_string(store_location):
    #     return JsonResponse({'validation':'enter valid location,must be a string'})
    # elif valid_string(store_address) :
    #     return JsonResponse({'validation':'enter valid address,must be a string'})
    # elif valid_float(store_latitude):
    #     return JsonResponse({'validation':'enter valid latitude,must be a float'})
    # elif valid_float(store_longitude) :
    #     return JsonResponse({'validation':'enter valid longitude,must be a float'})
    # elif valid_string(store_city) :
    #     return JsonResponse({'validation':'enter valid city,must be a string'})
    # elif valid_string(store_state) :
    #     return JsonResponse({'validation':'enter valid state,must be a string'})
    # elif valid_image(store_image) :
    #     return JsonResponse({'validation':'select valid image file,must be a valid format'})

    # try:
    #     with transaction.atomic():

    #         create_obj = Store.objects.create(
    #             store_name = store_name,
    #             store_location = store_location,
    #             store_address = store_address,
    #             store_latitude =  store_latitude,
    #             store_longitude = store_longitude,
    #             store_city = store_city,
    #             store_state = store_state,
    #             store_image = store_image
    #         )
    #         return JsonResponse({'validation':'success','status':True})
    # except Exception as e:
    #     return JsonResponse({'validation':str(e),'status':False})   
        #  ************************************************************************************************

def create_category(request):
    status, message, data = validate_create_category(request)
    # print( status, message, data)
    # print(status, message, data)
    if  status==False:
        return JsonResponse({"validation": message, "status": status })
    # else:
        # return JsonResponse({"validation": message, "status": status })

    category_data, status = create_category_function(data)
    # print("hhshsh",category_data, status)
    if status:
        return JsonResponse({'validation message' : "successful", "status" : status })
    else:
        return JsonResponse({'validation message' : "unsuccessful", "status" :status })

    # def create_category(request):
    #     params = request.POST
        
    #     store_id = params.get('store_id')
    #     category_name = params.get('category_name')
    #     category_image = request.FILES.get('category_image')

    #     if valid_integer(store_id):
    #         return JsonResponse({'validation':'enter valid store_id,must be a integer'})
    #     elif valid_string(category_name):
    #         return JsonResponse({'validation':'enter valid category_name,must be a string'})
    #     elif valid_image(category_image) :
    #         return JsonResponse({'validation':'select valid image file,must be a valid format'})
    
    #     store_obj = Store.objects.get(id= store_id)

    #     try:
    #         with transaction.atomic():

    #             category_obj = Category.objects.create(
    #                 store = store_obj,
    #                 category_name = category_name,
    #                 category_image = category_image
    #             )
    #             return JsonResponse({'validation':'success','status':True})
    #     except Exception as e:
    #         return JsonResponse({'validation':str(e),'status':False})
    #     # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def create_subcategory(request):
    status, message, data = validate_create_subcategory(request)
    if  status==False:
        return JsonResponse({"validation": message, "status": status })
    # else:
        # return JsonResponse({"validation": message, "status": status })

    subcategory_data, status = create_subcategory_function(data)
    if status:
        return JsonResponse({'validation message' : "successful", "status" : status })
    else:
        return JsonResponse({'validation message' : "unsuccessful", "status" :status })

    # def create_subcategory(request):
    #     params = request.POST
    
    #     store_id = params.get('store_id')
    #     category_id = params.get('category_id')
    #     subcategory_name = params.get('subcategory_name')
    #     subcategory_image = request.FILES.get('subcategory_image')

    #     if valid_integer(store_id):
    #         return JsonResponse({'validation':'enter valid store_id,must be a integer'})
    #     elif valid_integer(category_id):
    #         return JsonResponse({'validation':'enter valid category_name,must be a string'})
    #     elif valid_string(subcategory_name):
    #         return JsonResponse({'validation':'enter valid subcategory_name ,must be a string'})
    #     elif valid_image(subcategory_image) :
    #         return JsonResponse({'validation':'select valid image file,must be a valid format'})

    #     store_obj = Store.objects.get(id= store_id)
    #     category_obj = Category.objects.get(id= category_id)

    #     try:
    #         with transaction.atomic():

    #             subcategory_obj = Subcategory.objects.create(
    #                 store = store_obj,
    #                 category = category_obj,
    #                 subcategory_name = subcategory_name,
    #                 subcategory_image = subcategory_image
    #             )
    #             return JsonResponse({'validation':'success','status':True})
    #     except Exception as e:
    #         return JsonResponse({'validation':str(e),'status':False})
        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def create_product(request):
    status, message, data = validate_create_product(request)
    if  status==False:
        return JsonResponse({"validation": message, "status": status })
    # else:
        # return JsonResponse({"validation": message, "status": status })

    product_data, status = create_product_function(data)
    if status:
        return JsonResponse({'validation message' : "successful", "status" : status })
    else:
        return JsonResponse({'validation message' : "unsuccessful", "status" :status })

    # def create_product(request):
    #     params = request.POST

    #     store_id = params.get('store_id')
    #     subcategory_id = params.get('subcategory_id')
    #     product_name = params.get('product_name')
    #     product_quantity = int(params.get('product_quantity'))
    #     product_price  = float(params.get('product_price'))
    #     print(type(product_price))
    #     product_discount_price = float(params.get('product_discount_price'))
    #     product_description = params.get('product_description')
    #     product_image = request.FILES.get('product_image')

    #     if valid_integer(store_id):
    #         return JsonResponse({'validation':'enter valid store id,must be a integer'})
    #     elif valid_integer(subcategory_id) :
    #         return JsonResponse({'validation':'enter valid subcategory_id ,must be a integer'})
    #     elif valid_string(product_name) :
    #         return JsonResponse({'validation':'enter valid product_name ,must be a string'})
    #     elif valid_integer(product_quantity) :
    #         return JsonResponse({'validation':'enter valid product_quantity ,must be a integer'})
    #     elif valid_float(product_price) :
    #         return JsonResponse({'validation':'enter valid product_price ,must be a float'})
    #     elif valid_float(product_discount_price) :
    #         return JsonResponse({'validation':'enter valid product_discount_price ,must be a float'})
    #     elif valid_string(product_description) :
    #         return JsonResponse({'validation':'enter valid product_description ,must be a string'})
    #     elif valid_image(product_image) :
    #         return JsonResponse({'validation':'select valid image file,must be a valid format'})

    #     store_obj = Store.objects.get(id= store_id)
    #     subcategory_obj = Subcategory.objects.get(id= subcategory_id)

    #     try:
    #         with transaction.atomic():

    #             product_obj = Product.objects.create(
    #                 store = store_obj,
    #                 subcategory = subcategory_obj,
    #                 product_name = product_name,
    #                 product_quantity = product_quantity,
    #                 product_price = product_price,
    #                 product_discount_price = product_discount_price,
    #                 product_description = product_description,
    #                 product_image = product_image
    #             )
    #             return JsonResponse({'validation':'success','status':True})
    #     except Exception as e:
    #         return JsonResponse({'validation':str(e),'status':False})
            # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def get_store_by_id(request):
    try:
        params = json.loads(request.body)
    except Exception as e:
        # print(e)
        return JsonResponse({"validation" : str(e), "status" : False})
    status, message, data = validate_get_store_by_id(params)
    # print(status, message, data)
    if status==False:
        return JsonResponse({"validation": message, "status": status })
    store_data, status, message = get_store_by_id_function(data)
    print( store_data, status, message)
    if status:
        return JsonResponse({'validation' : message, "data" : store_data})
    else:
        return JsonResponse({'validation' : message, "status" : status})
    #--------     
    # def get_store_by_id(request):
    #     params = json.loads(request.body)

    #     response=[]
    #     store_id = params.get('store_id')
    #     # print(type(store_id))
    #     if valid_integer(store_id) :
    #         return JsonResponse({'validation':'enter valid store id,must be a integer'})

    #     try:
    #         store_obj = Store.objects.get(id=store_id)
    #         response.append(store_obj.get_json())
    #         return JsonResponse({'validation':'success','response':response,'status':True})
    #     except Exception as e:
    #         return JsonResponse({'validation':str(e),'status':False})
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def get_category_by_id(request):
    try:
        params = json.loads(request.body)         
    except Exception as e:
        return JsonResponse({'validation':str(e),'status':False})

    status,message,data = validate_get_category_by_id(params)
    if status==False:
        return JsonResponse({'validation':message,'status':status})

    category_data,status,message = get_category_by_id_function(data)
    if status:
        return JsonResponse({'validation':message,'data':category_data})
    else:
         return JsonResponse({'validation':message,'data':status})


    # def get_category_by_id(request):
    #     params = json.loads(request.body)

    #     response = []
    #     category_id = params.get('category_id')

    #     if valid_integer(category_id) :
    #         return JsonResponse({'validation':'enter valid category id,must be a integer'})

    #     try:
    #         category_obj = Category.objects.get(id=category_id)
    #         response.append(category_obj.get_json())
    #         return JsonResponse({'validation':'success','response':response,'status':True})
    #     except Exception as e:
    #         return JsonResponse({'validation':str(e),'status':False})
    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def get_subcategory_by_id(request):
    # try:
    #     params = json.loads(request.body)         
    # except Exception as e:
    #     return JsonResponse({'validation':str(e),'status':False})

    status,message,data = validate_get_subcategory_by_id(request)
    print(status,message,data)
    if status==False:
        return JsonResponse({'validation':message,'status':status})
        
    subcategory_data,status,message = get_subcategory_by_id_function(data)
    print(subcategory_data,status,message)
    if status:
        return JsonResponse({'validation':message,'data':subcategory_data})
    else:
         return JsonResponse({'validation':message,'data':status})

    # def get_subcategory_by_id(request):
    #     params = json.loads(request.body)

    #     response = []
    #     subcategory_id = params.get('subcategory_id')

    #     if valid_integer(subcategory_id) :
    #         return JsonResponse({'validation':'enter valid subcategory id,must be a integer'})

    #     try:       
    #         subcategory_obj = Subcategory.objects.get(id=subcategory_id)
    #         response.append(subcategory_obj.get_json())
    #         return JsonResponse({'validation':'success','response':response,'status':True})
    #     except Exception as e:
    #         return JsonResponse({'validation':str(e),'status':False})
     # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def get_product_by_id(request):
    try:
        params = json.loads(request.body)         
    except Exception as e:
        return JsonResponse({'validation':str(e),'status':False})

    status,message,data = validate_get_product_by_id(params)
    if status==False:
        return JsonResponse({'validation':message,'status':status})

    product_data,status,message = get_product_by_id_function(data)
    if status:
        return JsonResponse({'validation':message,'data':product_data})
    else:
         return JsonResponse({'validation':message,'data':status})

    # def get_product_by_id(request):
    #     params = json.loads(request.body)

    #     response = []
    #     product_id = params.get('product_id')
        
    #     if valid_integer(product_id) :
    #         return JsonResponse({'validation':'enter valid product id,must be a integer'})

    #     try:       
    #         product_obj = Product.objects.get(id=product_id)
    #         response.append(product_obj.get_json())
    #         return JsonResponse({'validation':'success','response':response,'status':True})
    #     except Exception as e:
    #         return JsonResponse({'validation':str(e),'status':False})
        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def get_all_store(request):
    store_data, status, message = get_all_store_function()
    print( store_data, status, message)
    if status:
        return JsonResponse({'validation' : message, "data" : store_data})
    else:
        return JsonResponse({'validation' : message, "status" : False})
    # def get_all_store(request):
    #     response=[]

    #     try:
    #         all_store = Store.objects.all()

    #         for store in all_store:
    #             response.append(store.get_json())              
    #         return JsonResponse({'validation':'success','response':response,'status':True})
    #     except Exception as e:
    #         return JsonResponse({'validation':str(e),'status':False})
        #  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def get_all_category(request):
    category_data, status, message = get_all_category_function()
    print( category_data, status, message)
    if status:
        return JsonResponse({'validation' : message, "data" : category_data})
    else:
        return JsonResponse({'validation' : message, "status" : False})
    # def get_all_category(request):
    #     response = []

    #     try:
    #         category_obj = Category.objects.all()

    #         for category in category_obj:
    #             response.append(category.get_all_category())
    #         return JsonResponse({'validation':'success','response':response,'status':True})
    #     except Exception as e:
    #         return JsonResponse({'validation':str(e),'status':False})  
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def get_all_subcategory(request):
    subcategory_data, status, message = get_all_subcategory_function()
    print( subcategory_data, status, message)
    if status:
        return JsonResponse({'validation' : message, "data" : subcategory_data})
    else:
        return JsonResponse({'validation' : message, "status" : False})
    # def get_all_subcategory(request):
    #     response = []

    #     try:
    #         subcategory_obj = Subcategory.objects.all()

    #         for subcategory in subcategory_obj:
    #             response.append(subcategory.get_all_subcategory())
    #         return JsonResponse({'validation':'success','response':response,'status':True})
    #     except Exception as e:
    #         return JsonResponse({'validation':str(e),'status':False})   
    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def get_all_product(request):
    product_data, status, message = get_all_product_function()
    print( product_data, status, message)
    if status:
        return JsonResponse({'validation' : message, "data" : product_data})
    else:
        return JsonResponse({'validation' : message, "status" : False})
    #
    # def get_all_product(request):
    #     response = []

    #     try:
    #         product_obj = Product.objects.all()
    #         # print(product_obj)
    #         for product in product_obj:
    #                 response.append(product.get_all_product())
    #         return JsonResponse({'validation':'success','response':response,'status':True})
    #     except Exception as e:
    #         return JsonResponse({'validation':str(e),'status':False})
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def get_category_by_store_id(request):
    try:
        params = json.loads(request.body)         
    except Exception as e:
        return JsonResponse({'validation':str(e),'status':False})

    status,message,data = validate_get_category_by_store_id(params)
    print(status,message,data)
    if status==False:
        return JsonResponse({'validation':message,'status':status})

    category_data,status,message = get_category_by_store_id_function(data)
    print(status,message,category_data)

    if status:
        return JsonResponse({'validation':message,'data':category_data})
    else:
         return JsonResponse({'validation':message,'data':status})

    # def get_category_by_store_id(request):
    #     response = []
    #     params = json.loads(request.body)

    #     store_id = params.get('store_id')

    #     if valid_integer(store_id) :
    #         return JsonResponse({'validation':'enter valid store id,must be a integer'})

    #     try:
    #         store_obj = Store.objects.get(id= store_id)
    #         category_qs = Category.objects.filter(store = store_obj)

    #         for category in category_qs:
    #             response.append(category.get_category())
    #         return JsonResponse({'validation':'success','response':response,'status':True})
    #     except Exception as e:
    #         return JsonResponse({'validation':str(e),'status':False})  
    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def get_subcategory_by_category_id(request):
    try:
        params = json.loads(request.body)         
    except Exception as e:
        return JsonResponse({'validation':str(e),'status':False})

    status,message,data = validate_get_subcategory_by_category_id(params)
    # print(status,message,data)
    if status==False:
        return JsonResponse({'validation':message,'status':status})

    subcategory_data,status,message = get_subcategory_by_category_id_function(data)
    # print(status,message,subcategory_data)

    if status:
        return JsonResponse({'validation':message,'data':subcategory_data})
    else:
         return JsonResponse({'validation':message,'data':status})

    # def get_subcategory_by_category_id(request):
    #     response = []
    #     params = json.loads(request.body)

    #     category_id = params.get('category_id')

    #     if valid_integer(category_id) :
    #         return JsonResponse({'validation':'enter valid category id,must be a integer'})

    #     try:
    #         category_obj = Category.objects.get(id= category_id)
    #         subcategory_qs = Subcategory.objects.filter(category = category_obj)

    #         for subcategory in subcategory_qs:
    #             response.append(subcategory.get_subcategory())
    #         return JsonResponse({'validation':'success','response':response,'status':True})
    #     except Exception as e:
    #         return JsonResponse({'validation':str(e),'status':False})
     # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++  

def get_product_by_store_id(request):

    try:
        params = json.loads(request.body)         
    except Exception as e:
        return JsonResponse({'validation':str(e),'status':False})

    status,message,data = validate_get_product_by_store_id(params)
    # print(status,message,data)
    if status==False:
        return JsonResponse({'validation':message,'status':status})

    product_data,status,message =get_product_by_store_id_function(data)
    # print(status,message,category_data)

    if status:
        return JsonResponse({'validation':message,'data':product_data})
    else:
         return JsonResponse({'validation':message,'data':status})
             
    #    def get_products_by_store_id(request):
    #     params = json.loads(request.body)

    #     response = []
    #     store_id = params.get('store_id')

    #     if valid_integer(store_id) :
    #         return JsonResponse({'validation':'enter valid store id,must be a integer'})
    #     # or
    #     # subcategory_id = params.get('subcategory_id')

    #     try:       
    #         # store_obj = Store.objects.get(id=store_id)
    #         product_qs = Product.objects.filter(store = store_id)

    #         # product_qs = Product.objects.filter(subcategory = subcategory_id)
    #         for product in product_qs:
    #             response.append(product.get_json())
    #         return JsonResponse({'validation':'success','response':response,'status':True})
    #     except Exception as e:
    #         return JsonResponse({'validation':str(e),'status':False})
        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def update_store_by_field(request):
    status, message, data = validate_update_store_by_field(request)
    # print( status, message, data)
    # print(status)
    if status==False:
        return JsonResponse({"validation": message, "status": status })
    # else:
        # return JsonResponse({"validation": message, "status": status })

    store_data, status = update_store_by_field_function(data)
    print(status)
    if  status:
        # print(status)
        return JsonResponse({"validation message" : "successful", "status" : status })
    else:
        return JsonResponse({"validation message" : "unsuccessful", "status" :status })

    # def update_store_by_field(request):
    #     params = request.POST

    #     store_id = params.get('store_id')
    #     store_name = params.get('store_name')
    #     store_location = params.get('store_location')
    #     store_address = params.get('store_location')
    #     store_latitude = params.get('store_latitude')
    #     store_longitude = params.get('store_longitude')
    #     store_city = params.get('store_city')
    #     store_state = params.get('store_state')
    #     store_image = request.FILES.get('store_image')
        
    #     if valid_integer(store_id) :
    #         return JsonResponse({'validation':'enter valid store name,must be a integer'})
    #     elif valid_string(store_name) :
    #         return JsonResponse({'validation':'enter valid store name,must be a string'})   
    #     elif valid_string(store_location) :
    #         return JsonResponse({'validation':'enter valid location,must be a string'})
    #     elif valid_string(store_address) :
    #         return JsonResponse({'validation':'enter valid address,must be a string'})
    #     elif valid_float(store_latitude) :
    #         return JsonResponse({'validation':'enter valid latitude,must be a float'})
    #     elif valid_float(store_longitude):
    #         return JsonResponse({'validation':'enter valid longitude,must be a float'})
    #     elif valid_string(store_city) :
    #         return JsonResponse({'validation':'enter valid store city,must be a string'})
    #     elif valid_string(store_state) :
    #         return JsonResponse({'validation':'enter valid store state,must be a string'})
    #     elif valid_image(store_image) :
    #         return JsonResponse({'validation':'select valid image file,must be a valid format'})

    #     try:
    #         with transaction.atomic():
    #             store_obj = Store.objects.get(id = store_id)
    #             store_obj.id = store_id
    #             store_obj.store_name = store_name
    #             store_obj.store_location = store_location
    #             store_obj.store_address = store_address
    #             store_obj.store_latitude = store_latitude
    #             store_obj.store_longitude = store_longitude
    #             store_obj.store_city = store_city
    #             store_obj.store_state = store_state
    #             store_obj.store_image = store_image
    #             # store_obj.created_on = created_on
    #             store_obj.save()
    #             return JsonResponse({'validation':'success','status':True})
    #     except Exception as e:
    #         return JsonResponse({'validation':str(e),'status':False})
      #   ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def update_category_by_field(request):
    status, message, data = validate_update_category_by_field(request)
    if  status==False:
        return JsonResponse({"validation": message, "status": status })
    # else:
        # return JsonResponse({"validation": message, "status": status })

    product_data, status = upadte_category_by_field_function(data)
    if status:
        return JsonResponse({'validation message' : "successful", "status" : status })
    else:
        return JsonResponse({'validation message' : "unsuccessful", "status" :status })

    # def update_category_by_field(request):
    #     params = request.POST
        
    #     category_id = params.get('category_id')
    #     store_id = params.get('store_id')
    #     category_name = params.get('category_name')
    #     category_image = request.FILES.get('category_image')

    #     if valid_integer(store_id):
    #         return JsonResponse({'validation':'enter valid store id,must be a integer'})
    #     elif valid_string(category_name):
    #         return JsonResponse({'validation':'enter valid category_name ,must be a string'})
    #     elif valid_string(category_name):
    #         return JsonResponse({'validation':'enter valid category_name ,must be a string'})    
    #     elif valid_image(category_image) :
    #         return JsonResponse({'validation':'select valid image file,must be a valid format'})

    #     store_obj = Store.objects.get(id= store_id)

    #     try:
    #         with transaction.atomic():

    #             category_obj = Category.objects.get(id = category_id)

    #             category_obj.store = store_obj
    #             category_obj.id = category_id
    #             category_obj.category_name = category_name
    #             category_obj.category_image = category_image
    #             category_obj.save()
    #             return JsonResponse({'validation':'success','status':True})
    #     except Exception as e:
    #         return JsonResponse({'validation':str(e),'status':False})
    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def update_subcategory_by_field(request):
    status, message, data = validate_update_subcategory_by_field(request)
    print(status)
    if  status==False:
        return JsonResponse({"validation": message, "status": status })
    # else:
        # return JsonResponse({"validation": message, "status": status })

    subcategory_data, status = upadte_subcategory_by_field_function(data)
    print(status)
    if status:
        return JsonResponse({'validation message' : "successful", "status" : status })
    else:
        return JsonResponse({'validation message' : "unsuccessful", "status" :status })
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    # def update_subcategory_by_field(request):
    #     params = request.POST
        
    #     # store_id = params.get('store_id')
    #     category_id = params.get('category_id')
    #     subcategory_id = params.get('subcategory_id')
    #     subcategory_name = params.get('subcategory_name')
    #     subcategory_image = request.FILES.get('subcategory_image')

    #     if valid_integer(category_id):
    #         return JsonResponse({'validation':'enter valid category id,must be a integer'})
    #     elif valid_integer(subcategory_id):
    #         return JsonResponse({'validation':'enter valid subcategory_id ,must be a integer'})
    #     elif valid_string(subcategory_name):
    #         return JsonResponse({'validation':'enter valid subcategory_name ,must be a string'})
    #     elif valid_image(subcategory_image) :
    #         return JsonResponse({'validation':'select valid image file,must be a valid format'})

    #     # store_obj = Store.objects.get(id= store_id)
    #     category_obj = Category.objects.get(id= category_id)

    #     try:
    #         with transaction.atomic():

    #             subcategory_obj = Subcategory.objects.get(id = subcategory_id) 
    #                 # store = store_obj,
    #             subcategory_obj.category = category_obj
    #             subcategory_obj.subcategory_name = subcategory_name
    #             subcategory_obj.subcategory_image = subcategory_image
    #             subcategory_obj.save()
    #             return JsonResponse({'validation':'success','status':True})
    #     except Exception as e:
    #         return JsonResponse({'validation':str(e),'status':False})
     # # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def update_product_by_field(request):
    status, message, data = validate_update_product_by_field(request)
    print(status)
    if  status==False:
        return JsonResponse({"validation": message, "status": status })
    # else:
        # return JsonResponse({"validation": message, "status": status })

    product_data, status = upadte_product_by_field_function(data)
    # print(product_data['id'])
    print(status)
    if status:
        return JsonResponse({'validation message' : "successful", "status" : status })
    else:
        return JsonResponse({'validation message' : "unsuccessful", "status" :status })

    # def update_product_by_field(request):

    #     params = request.POST

    #     # store_id = params.get('store_id')
    #     product_id = params.get('product_id')
    #     subcategory_id = params.get('subcategory_id')
    #     product_name = params.get('product_name')
    #     product_quantity = params.get('product_quantity')
    #     product_price  = params.get('product_price')
    #     product_discount_price = params.get('product_discount_price')
    #     product_description= params.get('product_description')
    #     product_image = request.FILES.get('product_image')

    #     if valid_integer(product_id):
    #         return JsonResponse({'validation':'enter valid store id,must be a integer'})
    #     elif valid_integer(subcategory_id):
    #         return JsonResponse({'validation':'enter valid subcategory_id ,must be a integer'})
    #     elif valid_string(product_name):
    #         return JsonResponse({'validation':'enter valid product_name ,must be a string'})
    #     elif valid_integer(product_quantity):
    #         return JsonResponse({'validation':'enter valid product_quantity ,must be a integer'})
    #     elif valid_float(product_price):
    #         return JsonResponse({'validation':'enter valid product_price ,must be a float'})
    #     elif valid_float(product_discount_price):
    #         return JsonResponse({'validation':'enter valid product_discount_price ,must be a float'})
    #     elif valid_string(product_description):
    #         return JsonResponse({'validation':'enter valid product_description ,must be a string'})
    #     elif valid_image(product_image) :
    #         return JsonResponse({'validation':'select valid image file,must be a valid format'})

    #     # store_obj = Store.objects.get(id= store_id)
    #     subcategory_obj = Subcategory.objects.get(id= subcategory_id)

    #     try:
    #         with transaction.atomic():

    #             product_obj = Product.objects.get(id = product_id)
    #             print(product_obj)
    #                 # product_obj.store = store_obj,
    #             product_obj.subcategory = subcategory_obj
    #             product_obj.id = product_id
    #             product_obj.product_name = product_name
    #             product_obj.product_quantity = product_quantity
    #             product_obj.product_price = product_price
    #             product_obj.product_discount_price = product_discount_price
    #             product_obj.product_description = product_description
    #             product_obj.product_image = product_image
    #             product_obj.save()
                
    #             return JsonResponse({'validation':'success','status':True})
    #     except Exception as e:
    #         return JsonResponse({'validation':str(e),'status':False})
     # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        
def delete_store_by_id(request):
    params = json.loads(request.body)

    store_id = params.get('store_id')

    if valid_integer(store_id):
        return JsonResponse({'validation':'enter valid store id,must be a integer'}) 

    try:
        store_obj = Store.objects.get(id= store_id).delete()
        return JsonResponse({'validation':'success','status':True})
    except Exception as e:
        return JsonResponse({'validation':str(e),'status':False})
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def delete_category_by_id(request):
    params = json.loads(request.body)

    category_id = params.get('category_id')
    if valid_integer(category_id):
        return JsonResponse({'validation':'enter valid category id,must be a integer'})
   
    try:
        category_obj = Category.objects.get(id= category_id).delete()
        return JsonResponse({'validation':'success','status':True})
    except Exception as e:
        return JsonResponse({'validation':str(e),'status':False})   
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def delete_subcategory_by_id(request):
    params = json.loads(request.body)

    subcategory_id = params.get('subcategory_id')
    if valid_integer(subcategory_id):
        return JsonResponse({'validation':'enter valid subcategory id,must be a integer'})
   
    try:
        subcategory_obj = Subcategory.objects.get(id= subcategory_id).delete()
        return JsonResponse({'validation':'success','status':True})
    except Exception as e:
        return JsonResponse({'validation':str(e),'status':False})   
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def delete_product_by_id(request):
    params = json.loads(request.body)

    product_id = params.get('product_id')

    if valid_integer(product_id):
        return JsonResponse({'validation':'enter valid product id,must be a integer'})
   
    try:
        product_obj = Product.objects.get(id = product_id).delete()
        return JsonResponse({'validation':'success','status':True})
    except Exception as e:
        return JsonResponse({'validation':str(e),'status':False})   
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def add_follower_to_store(request):
    params = json.loads(request.body)

    store_id = params.get('store_id')
    user_id = params.get('user_id')

    if valid_integer(store_id):
        return JsonResponse({'validation':'enter valid store id,must be a integer'})
    if valid_integer(user_id):
        return JsonResponse({'validation':'enter valid user id,must be a integer'})
   
    try:
        with transaction.atomic():
            store_obj = Store.objects.get(id=store_id)
            user_obj = UserProfile.objects.get(id=user_id)

            followership_obj = Followership.objects.create(
                store = store_obj, 
                user = user_obj
                )
            # print(followership_obj)
            return JsonResponse({'validation':'success','status':True})
    except Exception as e:
        return JsonResponse({'validation':str(e), 'status':False})
        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def get_followers_by_store(request):
    params = json.loads(request.body)
    response = []

    store_id = params.get('store_id')
    if valid_integer(store_id):
        return JsonResponse({'validation':'enter valid store id,must be a integer'})
   
    try:
        store_obj = Store.objects.get(id=store_id)
        follower_obj = store_obj.follower.all()
        # print(follower_obj)
        for follower in follower_obj:
            response.append(follower.first_name)
        return JsonResponse({'validation':'success','response':response,'status':True})
    except Exception as e:
        return JsonResponse({'validation':str(e), 'status':False})
        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def get_stores_by_follower(request):
    params = json.loads(request.body)
    response = []

    user_id = params.get('user_id')

    if valid_integer(user_id):
        return JsonResponse({'validation':'enter valid user id,must be a integer'})
      
    try:
        user_obj = UserProfile.objects.get(id=user_id)
        stores = user_obj.followers.all()
        # print(stores)
        for following in stores:
            response.append(following.store_name)
        # print(response)
        return JsonResponse({'validation':'success','response':response,'status':True})
    except Exception as e:
        return JsonResponse({'validation':str(e), 'status':False})
    #  +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++   

def get_all_followers(request):
    response = []

    try:       
        user_obj = Followership.objects.all()
        
        for followers in user_obj:
            response.append(followers.user.first_name)
        return JsonResponse({'validation':'success','response':response,'status':True})
    except Exception as e:
        return JsonResponse({'validation':str(e),'status':False})
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++        

def remove_follower_from_store(request):
    params = json.loads(request.body)

    followership_id = params.get('followership_id')

    if valid_integer(followership_id):
        return JsonResponse({'validation':'enter valid followership id,must be a integer'})   
    
    try:
        followership_obj = Followership.objects.get(id=followership_id)
        followership_obj.user==None
        followership_obj.savef()
        return JsonResponse({'validation':'success','status':True})
    except Exception as e:
        return JsonResponse({'validation':str(e), 'status':False})
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def remove_follower_from_store_for_some_reason(request):
    params = json.loads(request.body)

    followership_id = params.get('followership_id')
    reason = params.get('reason')

    if valid_integer(followership_id):
        return JsonResponse({'validation':'enter valid followership id,must be a integer'})
    if valid_integer(reason):
        return JsonResponse({'validation':'enter valid reason,must be a integer'})   
    
    try:
        followership_obj = Followership.objects.get(id=followership_id)
        followership_obj.user = None
        followership_obj.reason = reason
        followership_obj.save()
        
        return JsonResponse({'validation':'success','status':True,})
    except Exception as e:
        return JsonResponse({'validation':str(e), 'status':False})
    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
  






       

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











    
