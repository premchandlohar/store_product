# from django.http import JsonResponse
from django.core.validators import validate_email


def valid_string(string):
    if (type(string) != str) or (string ==""):
        return True
    else: 
        return False

def valid_float(float_data):
    if (type(float_data) != float) or (float_data ==""):
        return True
    else: 
        return False

def valid_integer(integer):
    if (type(integer) != int) or (integer ==""):
        return True
    else: 
        return False
    
def valid_pincode(integer):
    if (type(integer) != int) or (integer ==""):
        return True
    elif len(str(integer))!=6:
        return True
    else:
        return False

# def valid_email(email):
#     if (type(email) != str) or (email ==""):
#         return True
#     elif email:
#         not validate_email(email)
#         return True
#     else: 
#         return False

def valid_email(email):
    if (type(email) != str) or (email ==""):
        return True
    elif not '@' in email:
        return True
    elif not '.com' in email:
        return True   
    else: 
        return False

# def valid_email(email):
#     if (type(email) != str) or (email ==""):
#         return True
#     elif not '@' or '.com' in email:
#         return True
#     # elif not '.com' in email:
#     #     return True   
#     else: 
#         return False




# elif type(store_location) != str:
#     return JsonResponse({'validation':'enter valid location,must be a string'})
# elif type(store_address) != str:
#     return JsonResponse({'validation':'enter valid address,must be a string'})
# elif type(store_latitude) !=float:
#     return JsonResponse({'validation':'enter valid latitude,must be a float'})
# elif type(store_longitude) != float:
#     return JsonResponse({'validation':'enter valid longitude,must be a float'})
# elif type(store_city) != str:
#     return JsonResponse({'validation':'enter valid store city,must be a string'})
# elif type(store_state) != str:
#     return JsonResponse({'validation':'enter valid store state,must be a string'})
