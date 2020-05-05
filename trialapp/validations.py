from .models import *
from django.db import transaction
from validator import *
import json

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
    
def validate_get_category_by_id(params):
    try:
        category_id = int(params.get("category_id"))

        if valid_integer(category_id): return True,'enter valid category_id,must be a integer',None
        
        kwarg = {
            "category_id":category_id
        }
        return True, "validation successfully",kwarg

    except Exception as e:
        # print(e)
        return False, str(e), None
 
       # -----------------------------------validate get Subcategory by id------------------------------

def validate_get_subcategory_by_id(request):
    try:
        params = json.loads(request.body)         
    # except Exception as e:
    #     return ({'validation':str(e),'status':False,None})

    # try:
        subcategory_id = int(params.get("subcategory_id"))

        if valid_integer(subcategory_id): return True,'enter valid subcategory_id,must be a integer',None
        
        kwarg = {
            "subcategory_id":subcategory_id
        }
        return True, "validation successfully",kwarg

    except Exception as e: return False, str(e), None

    # -----------------------------------validate get product by id----------------------------------
   
def validate_get_product_by_id(params):
    try:
        product_id = int(params.get("product_id"))

        if valid_integer(product_id): return True,'enter valistore_idd product_id,must be a integer',None
        
        kwarg = {
            "product_id":product_id
        }
        return True, "validation successfully",kwarg

    except Exception as e:
        # print(e)
        return False, str(e), None
 
 # -------------------------------validate get product by store id-----------------------------

def validate_get_category_by_store_id(params):
    try:
        store_id = int(params.get("store_id"))
        if valid_integer(store_id): return True,'enter valid store_id,must be a integer',None

        kwarg = {
            "store_id":store_id
        }
        return True, "validation successfully",kwarg

    except Exception as e:
        # print(e)
        return False, str(e), None
 
    # ---------------------------------validate get subcategory by Category id----------------------------

def validate_get_subcategory_by_category_id(params):
    try:
        category_id = int(params.get("category_id"))
        if valid_integer(category_id): return True,'enter valid category_id,must be a integer',None

        kwarg = {
            "category_id":category_id
        }
        return True, "validation successfully",kwarg

    except Exception as e:
        # print(e)
        return False, str(e), None

    # ----------------------------------validate get product by store id---------------------------------

def validate_get_product_by_store_id(params):
    try:
        store_id = int(params.get("store_id"))
        if valid_integer(store_id): return True,'enter valid store_id,must be a integer',None

        kwarg = {
            "store_id":store_id
        }
        return True, "validation successfully",kwarg

    except Exception as e:
        # print(e)
        return False, str(e), None

        # -------------------------- validate update store--------------------------------------------------

def validate_update_store_by_field(request):
    params = request.POST
    try:
        store_id = int(params.get('store_id'))
        store_name = params.get('store_name')
        store_location = params.get('store_location')
        store_address = params.get('store_address')
        store_latitude = float(params.get('store_latitude'))
        store_longitude = float(params.get('store_longitude'))
        store_city = params.get('store_city')
        store_state = params.get('store_state')
        store_image = request.FILES.get('store_image')

        if valid_integer(store_id):
            return True,'enter valid store id,must be integer',None
        elif valid_string(store_name):
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
            "store_id":store_id,
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

     # -----------------------------------vallidate update category-----------------------------------------------------------------

def validate_update_category_by_field(request):
    params = request.POST

    try:
        store_id = int(params.get('store_id'))
        category_id = int(params.get('category_id'))
        category_name = params.get('category_name')
        category_image = request.FILES.get('category_image')
        # print(category_image)

        if valid_integer(store_id):
            return True,'enter valid store_id,must be a integer',None
        elif valid_integer(category_id):
            return True,'enter valid category_id,must be a integer',None     
        elif valid_string(category_name):
            return True,'enter valid category_name,must be a string',None
            # print(valid_string(category_name))
        elif valid_image(category_image):
            return True,'select valid image file,must be a valid format',None
            # print(valid_image(category_image))


        kwarg = {
            "store_id":store_id,
            "category_id":category_id,
            "category_name":category_name,
            "category_image":category_image

        }
        print(kwarg)

        return True, "validation successfully",kwarg
    
    except Exception as e:
        # print(e)
        return False, str(e), None

        # ---------------------------------validate update Subcategory------------------------------------

def validate_update_subcategory_by_field(request):
    params = request.POST

    try:
        category_id = int(params.get('category_id'))
        print(category_id)
        subcategory_id = int(params.get('subcategory_id'))
        subcategory_name = params.get('subcategory_name')
        print(subcategory_name)
        subcategory_image = request.FILES.get('subcategory_image')
        # print(category_image)

        if valid_integer(category_id):
            return True,'enter valid category_id,must be a integer',None
        elif valid_integer(subcategory_id):
            return True,'enter valid subcategory_id,must be a integer',None     
        elif valid_string(subcategory_name):
            return True,'enter valid subcategory_name,must be a string',None
            # print(valid_string(subcategory_name))
        elif valid_image(subcategory_image):
            return True,'select valid image file,must be a valid format',None
            # print(valid_image(category_image))


        kwarg = {            
            "category_id":category_id,
            "subcategory_id":subcategory_id,
            "subcategory_name":subcategory_name,
            "subcategory_image":subcategory_image
        }

        print(kwarg)

        return True, "validation successfully",kwarg
    
    except Exception as e:
        # print(e)
        return False, str(e), None

        # ---------------------------------validate update product------------------------------------

def validate_update_product_by_field(request):
    params = request.POST

    try:
        store_id = int(params.get('store_id'))
        subcategory_id = int(params.get('subcategory_id'))
        product_id = int(params.get('product_id'))
        product_name = params.get('product_name')
        product_quantity = int(params.get('product_quantity'))
        product_price  = float(params.get('product_price'))
        # print(type(product_price))
        product_discount_price = float(params.get('product_discount_price'))
        product_description = params.get('product_description')
        product_image = request.FILES.get('product_image')

        if valid_integer(store_id):
            return True,'enter valid store id,must be a integer',None
        if valid_integer(subcategory_id) :
            return True,'enter valid subcategory_id ,must be a integer',None
        elif valid_integer(product_id) :
            return True,'enter valid product_id ,must be a integer',None
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
            "product_id":product_id,
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

        # ---------------------------------validate_delete_store_by_id------------------------------------

def validate_delete_store_by_id(params):
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

             # ---------------------------------validate_delete_category_by_id------------------------------------

def validate_delete_category_by_id(params):
    try:
        category_id = int(params.get('category_id'))

        if valid_integer(category_id):
            return True,'enter valid category id,must be a integer',None

        kwarg = {
            "category_id":category_id
        }
        return True, "validation successfully",kwarg

    except Exception as e:
        # print(e)
        return False, str(e), None

          # ---------------------------------validate_delete_subcategory_by_id------------------------------------

def validate_delete_subcategory_by_id(params):
    try:
        subcategory_id = int(params.get('subcategory_id'))

        if valid_integer(subcategory_id):
            return True,'enter valid subcategory id,must be a integer',None

        kwarg = {
            "subcategory_id":subcategory_id
        }
        return True, "validation successfully",kwarg

    except Exception as e:
        # print(e)
        return False, str(e), None

          # ---------------------------------validate_delete_product_by_id------------------------------------

def validate_delete_product_by_id(params):
    try:
        product_id = int(params.get('product_id'))

        if valid_integer(product_id):
            return True,'enter valid product id,must be a integer',None

        kwarg = {
            "product_id":product_id
        }
        return True, "validation successfully",kwarg

    except Exception as e:
        # print(e)
        return False, str(e), None

        # --------------------------validate add follower to store--------------------------------

def validate_add_follower_to_store(params):
    try:
        store_id = int(params.get('store_id'))
        user_id = int(params.get('user_id'))

        if valid_integer(store_id):
            return True,'enter valid store_id,must be a integer',None
        if valid_integer(user_id):
            return True,'enter valid user_id,must be a integer',None

        kwarg = {
            "store_id":store_id,
            "user_id":user_id
        }

        return True, "validation successfully",kwarg

    except Exception as e:
        # print(e)
        return False, str(e), None

        # -------------------------------validate get followers by store--------------------------------

def validate_get_followers_by_store(params):
    try:
        store_id = int(params.get('store_id'))
        # user_id = int(params.get('user_id'))

        if valid_integer(store_id):
            return True,'enter valid store_id,must be a integer',None

        kwarg = {
            "store_id":store_id
        }
            
        return True, "validation successfully",kwarg

    except Exception as e:
        # print(e)
        return False, str(e), None

     # -------------------------------validate get stores by follower--------------------------------

def validate_get_stores_by_follower(params):
    try:
        user_id = int(params.get('user_id'))
        # user_id = int(params.get('user_id'))

        if valid_integer(user_id):
            return True,'enter valid user_id,must be a integer',None

        kwarg = {
            "user_id":user_id
        }
            
        return True, "validation successfully",kwarg

    except Exception as e:
        # print(e)
        return False, str(e), None

        # -------------------------------remove_follower_from_store_for_some_reason-------------------------

def validate_remove_follower_from_store_for_some_reason(params):
    try:
        followership_id = int(params.get('followership_id'))
        reason = int(params.get('reason'))
        if valid_integer(followership_id):
            return True,'enter valid followership_id,must be a integer',None
        if valid_integer(reason):
            return True,'enter valid reason,must be a integer',None

        kwarg = {
            "followership_id":followership_id,
            "reason":reason
        }
      
        return True, "validation successfully",kwarg

    except Exception as e:
        # print(e)
        return False, str(e), None

