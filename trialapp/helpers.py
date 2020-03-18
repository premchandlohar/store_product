from .models import *
from django.db import transaction

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
        store_data = Store.objects.get(id=data['Store_id'])
        data = store_data.get_json()
        print(data)

        return data,True,'successful'
    # except ObjectDoesNotExist:
    #     return None, False, "Invalid Id"

    except Exception as e:
        return None,False,'unsuccessful'
