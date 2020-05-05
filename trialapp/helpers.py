from .models import *
from django.db import transaction
from django.core.exceptions import ObjectDoesNotExist
# from new_users.models import *


def create_store_function(data):
    try:
        with transaction.atomic():
            store_data = Store.objects.create(
                store_name = data['store_name'],
                store_location = data['store_location'],
                store_address = data['store_address'],
                store_latitude =  data['store_latitude'],
                store_longitude = data['store_longitude'],
                store_city = data['store_city'],
                store_state = data['store_state'],
                store_image = data['store_image']
            )
        return {'store data':store_data},True
    except Exception as e:
        return None,False
    # return {'store data':store_data},True

        # ----------------------------------create Category---------------------------------------------------

def create_category_function(data):
    try:
        store = Store.objects.get(id=data["store_id"])
        with transaction.atomic():

            category_data = Category.objects.create(
                store = store,
                category_name = data['category_name'],
                category_image = data['category_image']
            )
        return {'category data':category_data},True
    except Exception as e:
        return None,False

        # --------------------------------------create Subcategory-------------------------------------

def create_subcategory_function(data):
    try:
        store_data = Store.objects.get(id=data['store_id'])
        category_data =Category.objects.get(id=data['category_id'])
        
        with transaction.atomic():

            subcategory_data = Subcategory.objects.create(
                store = store_data,
                category = category_data,
                subcategory_name = data['subcategory_name'],
                subcategory_image = data['subcategory_image']
            )
        return {'subcategory data':subcategory_data},True
    except Exception as e:
        return None,False

    #   ----------------------------------create product--------------------------------------------------------

def create_product_function(data):
    try:
        store_data = Store.objects.get(id=data['store_id'])
        subcategory_data =Subcategory.objects.get(id=data['subcategory_id'])
        
        with transaction.atomic():

             product_data = Product.objects.create(
                store = store_data,
                subcategory = subcategory_data,
                product_name = data['product_name'],
                product_quantity = data['product_quantity'],
                product_price = data['product_price'],
                product_discount_price = data['product_discount_price'],
                product_description = data['product_description'],
                product_image = data['product_image']
            )
        return {'subcategory data':product_data},True
    except Exception as e:
        return None,False

        # --------------------------------------get store by id-------------------------------------------------------------

def get_store_by_id_function(data):
    try:
        store_data = Store.objects.get(id=data['store_id'])
        data = store_data.get_json()
        print(data)

        return data,True,'successful'
    except ObjectDoesNotExist:
        return None, False, "Invalid Id"

    except Exception as e:
        return None,False,'unsuccessful'

        # --------------------------------------get category by id-------------------------------------------------------------

def get_category_by_id_function(data):
    try:
        category_data = Category.objects.get(id=data['category_id'])
        data = category_data.get_json()

        return data,True,'successful'
    except ObjectDoesNotExist:
        return None, False, "Invalid Id"

    except Exception as e:
        return None,False,'unsuccessful'

        # -----------------------get subcategory by id------------------------------------------------

def get_subcategory_by_id_function(data):
    try:
        subcategory_data = Subcategory.objects.get(id=data['subcategory_id'])
        data = subcategory_data.get_json()
        # print(data)

        return data,True,'successful'
    except ObjectDoesNotExist:
        return None, False, "Invalid Id"

    except Exception as e:
        return None,False,'unsuccessful'

        # -------------------------get product by id------------------------------------------------

def get_product_by_id_function(data):
    try:
        product_data = Product.objects.get(id=data['product_id'])
        data = product_data.get_json()

        return data,True,'successful'
    except ObjectDoesNotExist:
        return None, False, "Invalid Id"

    except Exception as e:
        return None,False,'unsuccessful'

        # ------------------------get all store---------------------------------------------------

def get_all_store_function():
    data=[]
    try:
        store_data =Store.objects.all()
        for store in store_data:
            data.append(store.get_json())

        return data,True,'successful'
    except ObjectDoesNotExist:
        return None, False, "Invalid Id"

    except Exception as e:
        return None,False,'unsuccessful'

        # ------------------------get all category---------------------------------------------------

def get_all_category_function():
    data=[]
    try:
        category_data =Category.objects.all()
        for category in category_data:
            data.append(category.get_all_category())

        return data,True,'successful'
    except ObjectDoesNotExist:
        return None, False, "Invalid Id"

    except Exception as e:
        return None,False,'unsuccessful'

      # ------------------------get all subcategory---------------------------------------------------

def get_all_subcategory_function():
    data=[]
    try:
        subcategory_data =Subcategory.objects.all()
        for subcategory in subcategory_data:
            data.append(subcategory.get_all_subcategory())

        return data,True,'successful'
    except ObjectDoesNotExist:
        return None, False, "Invalid Id"

    except Exception as e:
        return None,False,'unsuccessful'

    # -----------------------------get all product------------------------------------------------------

def get_all_product_function():
    data=[]
    try:
        product_data =Product.objects.all()
        for product in product_data:
            data.append(product.get_all_product())

        return data,True,'successful'
    except ObjectDoesNotExist:
        return None, False, "Invalid Id"

    except Exception as e:
        return None,False,'unsuccessful'

        # ----------------------------get category by store id-----------------------------------------

def get_category_by_store_id_function(data):
    try:
        response = []
        print(data)
        category_data = Category.objects.filter(store=data['store_id'])
        print(category_data)
        for obj in category_data:
            response.append(obj.get_json())
        
        # response=[]
        # store_obj = Store.objects.get(id=data['store_id'])
        # category_data = Category.objects.filter(store=store_obj)
        # for obj in category_data:
        #     obj.append (data.get_json())

        return response,True,'successful'
    except ObjectDoesNotExist:
        return None, False, "Invalid Id"

    except Exception as e:
        return None,False,'unsuccessful'

    #   ---------------------------get subcataegory by category id-----------------------------------------

def get_subcategory_by_category_id_function(data):
    try:
        response =[]
        subcategory_data = Subcategory.objects.filter(category=data['category_id'])
        for obj in subcategory_data:
            response.append(obj.get_json())

        return response,True,'successful'
    except ObjectDoesNotExist:
        return None, False, "Invalid Id"

    except Exception as e:
        return None,False,'unsuccessful'

        # -----------------------------get product by store id-------------------------------------------------------------

def get_product_by_store_id_function(data):
    try:
        response =[]
        category_data = Category.objects.filter(store=data['store_id'])
        for obj in category_data:
            response.append(obj.get_json())

        return response,True,'successful'
    except ObjectDoesNotExist:
        return None, False, "Invalid Id"

    except Exception as e:
        return None,False,'unsuccessful'

        # ---------------------------------upadte store by field----------------------------------------

def update_store_by_field_function(data):
    try:
        with transaction.atomic():
        
            store_data = Store.objects.get(id =data['store_id'])
            # print(store_data)

            # store_data.id = data['store_id
            store_data.store_name = data['store_name']
            # print( data['store_name'])
            store_data.store_location = data['store_location']
            store_data.store_address =data['store_address']
            store_data.store_latitude = data['store_latitude']
            store_data.store_longitude =data['store_longitude']
            store_data.store_city = data['store_city']
            store_data.store_state = data['store_state']
            store_data.store_image = data['store_image']
            # print(store_data.store_name)
            # store_data.created_on = data['created_on']
            store_data.save()
            # print(store_data)
        return {'store data':store_data},True
    except Exception as e:
        return None,False
        
        # ----------------------------------update Category by field---------------------------------------------------

def upadte_category_by_field_function(data):
    try:
        with transaction.atomic():
            store_data = Store.objects.get(id=data["store_id"])
            category_data = Category.objects.get(id=data["category_id"])

            category_data.store = store_data
            category_data.category_name = data['category_name']
            category_data.category_image = data['category_image']
            category_data.save()
           
        return {'category data':category_data},True
    except Exception as e:
        return None,False

    # ---------------------------------update subCategory by field---------------------------------------------------

def upadte_subcategory_by_field_function(data):
    try:
        with transaction.atomic():
            category_data = Category.objects.get(id=data["category_id"])
            subcategory_data = Subcategory.objects.get(id=data["subcategory_id"])

            subcategory_data.category = category_data
            subcategory_data.subcategory_name = data['subcategory_name']
            subcategory_data.subcategory_image = data['subcategory_image']
            subcategory_data.save()
           
        return {'category data':category_data},True
    except Exception as e:
        return None,False

        # ---------------------------update product by field--------------------------------------------

def upadte_product_by_field_function(data):
    try:
        with transaction.atomic():
            store_data = Store.objects.get(id=data['store_id'])
            subcategory_data = Subcategory.objects.get(id=data["subcategory_id"])
            product_data = Product.objects.get(id=data["product_id"])

            product_data.store: store_data
            product_data.subcategory: subcategory_data
            # product_data.product_id: product_id
            product_data.product_name= data['product_name']
            product_data.product_quantity= data['product_quantity']
            product_data.product_price= data['product_price']
            product_data.product_discount_price= data['product_discount_price']
            product_data.product_description= data['product_description']
            product_data.product_image= data['product_image']
            product_data.save()

            return {'category data':product_data},True
    except Exception as e:
        return None,False

        # ------------------------delete store by id----------------------------------------------

def delete_store_by_id_function(data):
    try:
        store_data = Store.objects.get(id=data['store_id']).delete()
        return 'successfully delete',True
    except ObjectDoesNotExist :
        return "invalid id", False

    except Exception as e:
        return None,False

          # ------------------------delete category by id----------------------------------------------

def delete_category_by_id_function(data):
    try:
        category_data = Category.objects.get(id=data['category_id']).delete()
        return 'successfully delete',True
    except ObjectDoesNotExist :
        return "invalid id", False

    except Exception as e:
        return None,False
        
               # ------------------------delete subcategory by id----------------------------------------------

def delete_subcategory_by_id_function(data):
    try:
        subcategory_data = Subcategory.objects.get(id=data['subcategory_id']).delete()
        return 'successfully delete',True
    except ObjectDoesNotExist :
        return "invalid id", False

    except Exception as e:
        return None,False

                 # ------------------------delete product by id----------------------------------------------

def delete_product_by_id_function(data):
    try:
        product_data = Product.objects.get(id=data['product_id']).delete()
        return 'successfully delete',True
    except ObjectDoesNotExist :
        return "invalid id", False

    except Exception as e:
        return None,False

            # ------------------------add follower to store----------------------------------------------

def add_follower_to_store_function(data):
    try:
        store_data = Store.objects.get(id=data['store_id'])
        user_data = UserProfile.objects.get(id=data['user_id'])

        follower_data = Followership.objects.create(
                store = store_data,
                user =user_data
            )
                
        return {'follower_data':follower_data},True
    except Exception as e:
        return None,False

         # ------------------------get followers by store----------------------------------------------

def get_followers_by_store_function(data):
    try:
        response =[]
        store_data = Store.objects.get(id=data['store_id'])
        follower_data = store_data.follower.all()

        for follower in follower_data:
            response.append(follower.first_name)
        return {'follower_data':response},True
        
    except ObjectDoesNotExist:
        return 'no followers',False
    except Exception as e:
        return None,False

         # ------------------------add follower to store----------------------------------------------

def get_stores_by_follower_function(data):
    try:
        response =[]
        user_data = UserProfile.objects.get(id=data['user_id'])
        store_data = user_data.followers.all()

        for store in store_data:
            response.append(store.store_name)
        return {'store':response},True

    except ObjectDoesNotExist:
        return 'no following',False   
    except Exception as e:
        return None,False

           # ------------------------add follower to store----------------------------------------------

def get_all_followers_function():
    try:
        response =[]
        follower_data = Followership.objects.all()
        # print("follower_data",follower_data)

        for followers in follower_data:
            # print('ggg',followers)
            response.append(followers.get_json())
        # print(response)
        return response,True,'successful'
   
    except Exception as e:
        return None,False,'unsuccessful' 

        # -------------def remove_follower_from_store_for_some_reason_function----------------------

def remove_follower_from_store_for_some_reason_function(data):
    try:
        followership_data = Followership.objects.get(id=data['followership_id'])
        followership_data.user = None
        followership_data.reason = data['reason']
        followership_data.save()
            
        return 'success',True
 
    except Exception as e:
        return 'unsuccess',False

