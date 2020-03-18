from .models import *
from django.db import transaction
from validator import *

def validate_create_store(request):
    params = request.POST
    try:
        store_name = params.get('store_name')
        store_location = params.get('store_location')
        store_address = params.get('store_address')
        store_latitude = float(params.get('store_latitude'))
        store_longitude = float(params.get('store_longitude'))
        store_city = params.get('store_city')
        store_state = params.get('store_state')
        store_image = request.FILES.get('store_image')

        if valid_string(store_name):
            return True,'enter valid store name,must be a string',None
        elif valid_string(store_location):
            return True,'enter valid location,must be a string',None
        elif valid_string(store_address) :
            return True,'enter valid address,must be a string',None
        elif valid_float(store_latitude):
            return True,'enter valid latitude,must be a float',None
        elif valid_float(store_longitude) :
            return True,'enter valid longitude,must be a float',None
        elif valid_string(store_city) :
            return True,'enter valid city,must be a string',None
        elif valid_string(store_state) :
            return True,'enter valid state,must be a string',None
        elif valid_image(store_image) :
            return True,'select valid image file,must be a valid format',None

        kwarg={
            "store_name":store_name,
            "store_location":store_location,
            "store_address":store_address,
            "store_latitude":store_latitude,
            "store_longitude":store_longitude,
            "store_city":store_city,
            "store_state":store_state,
            "store_image":store_image

        }

        return True, "validation successfully",kwarg

    except Exception as e:
        # print(e)
        return False, str(e), None

     # -----------------------------------vallidate create category-----------------------------------------------------------------

def validate_create_category(request):
    params = request.POST

    try:
        store_id = int(params.get('store_id'))
        category_name = params.get('category_name')
        category_image = request.FILES.get('category_image')
        # print(category_image)

        if valid_integer(store_id):
            return True,'enter valid store_id,must be a integer',None
        elif valid_string(category_name):
            return True,'enter valid category_name,must be a string',None
            # print(valid_string(category_name))
        elif valid_image(category_image):
            return True,'select valid image file,must be a valid format',None
            # print(valid_image(category_image))


        kwarg = {
            "store_id":store_id,
            "category_name":category_name,
            "category_image":category_image

        }
        print(kwarg)

        return True, "validation successfully",kwarg
    
    except Exception as e:
        # print(e)
        return False, str(e), None

        # ---------------------------------validate create Subcategory------------------------------------

def validate_create_subcategory(request):
    params = request.POST

    try:
        store_id = int(params.get('store_id'))
        category_id =int(params.get('category_id'))
        subcategory_name = params.get('subcategory_name')
        subcategory_image = request.FILES.get('subcategory_image')

        if valid_integer(store_id):
            return True,'enter valid store_id,must be a integer',None
        elif valid_integer(category_id):
            return True,'enter valid category_id,must be a integer',None
        elif valid_string(subcategory_name):
            return True,'enter valid subcategory_name,must be a integer',None
        elif valid_image(subcategory_image) :
            return True,'select valid image file,must be a valid format',None

        kwarg = {
            "store_id":store_id,
            "category_id":category_id,
            "subcategory_name":subcategory_name,
            "subcategory_image":subcategory_image

        }
        return True, "validation successfully",kwarg
    
    except Exception as e:
        # print(e)
        return False, str(e), None

        # -----------------------------------------------valildate product-------------------------------

def validate_create_product(request):
    params = request.POST

    try:
        store_id = int(params.get('store_id'))
        subcategory_id = int(params.get('subcategory_id'))
        product_name = params.get('product_name')
        product_quantity = int(params.get('product_quantity'))
        product_price  = float(params.get('product_price'))
        # print(type(product_price))
        product_discount_price = float(params.get('product_discount_price'))
        product_description = params.get('product_description')
        product_image = request.FILES.get('product_image')

        if valid_integer(store_id):
            return True,'enter valid store id,must be a integer',None
        elif valid_integer(subcategory_id) :
            return True,'enter valid subcategory_id ,must be a integer',None
        elif valid_string(product_name) :
            return True,'enter valid product_name ,must be a string',None
        elif valid_integer(product_quantity) :
            return True,'enter valid product_quantity ,must be a integer',None
        elif valid_float(product_price) :
            return True,'enter valid product_price ,must be a float',None
        elif valid_float(product_discount_price) :
            return True,'enter valid product_discount_price ,must be a float',None
        elif valid_string(product_description) :
            return True,'enter valid product_description ,must be a string',None
        elif valid_image(product_image) :
            return True,'select valid image file,must be a valid format',None

        kwarg={
            "store_id":store_id,
            "subcategory_id":subcategory_id,
            "product_name":product_name,
            "product_quantity":product_quantity,
            "product_price":product_price,
            "product_discount_price":product_discount_price,
            "product_description":product_description,
            "product_image":product_image

        }

        return True, "validation successfully",kwarg

    except Exception as e:
        # print(e)
        return False, str(e), None

        # --------------------------------------------validate get store by id-----------------------------
def validate_get_store_by_id(params):
    try:
        store_id = int(params.get('store_id'))

        if valid_integer(store_id):
            return True,'enter valid store id,must be a integer',None
        
        kwarg = {
            "store_id":store_id
        }

        return True, "validation successfully",kwarg

    except Exception as e:
        # print(e)
        return False, str(e), None

        # --------------------------------------------validate get category by id-----------------------------
    