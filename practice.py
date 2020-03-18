# from django.http import JsonResponse
# from validator import *

# user=input('enter a name:')
# user = 'ram'
# user = 'ram'
# email = input('enter email:')
# email = '111p.1rmj@fd1122gmai.hj'

# print('invalid' if email==None or not re.match(r"[^@]+@[^@]+\.[^@]+", email) or email=='' else 'valid')
# print('invalid' if email==None or not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
# , email) or email=='' else 'valid')


# if valid_string(user):
#     print('enter valid user,must be a string') 
# print('valid')  
# def valid_string(user):
# print (' valid input' if (type(user) == int) and (user !=None) and user!=''  else 'enter valid i/p' )
# print ('valid ' if isinstance(user,float) and (user !=None) and user!=''  else 'invalid' )
# print(type(email))  
# r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"

# def validate_pin(pin):
# pin='1414'
# if len(pin)==4:
#     a=pin.split()
#     # print(a)
#     # print( True for x in a isinstance(a,int) )
#     for int(x) in a:
#         print(type(x))
#         if isinstance(x,int):
#             print(True)
#         else:
#             print(False)
# else:
#     print(False) 



# from django.http import JsonResponse
# from django.core.validators import validate_email
import re


def valid_string(string):
     return (True if (type(string) != str) or (string ==None) or string==''  else False )

# print(valid_string(a))

def valid_float(float_data):
    return( True if not isinstance(float_data,float) or (float_data=='') or (float_data==None) else False )

# print(valid_float(a))


def valid_integer(integer):
    return (True if (type(integer) != int) or (integer ==None) or (integer=='')  else False )      
# a=1263411
def valid_pincode(integer):
    return( True if (type(integer) != int) or len(str(integer)) !=6 or (integer==None) else False )
# print(valid_pincode(a))
# def valid_email(email):
#     if (type(email) != str) or (email ==""):
#         return True
#     elif email:
#         not validate_email(email)
#         return True
#     else: 
#         return False

# def valid_email(email):
#     if (type(email) != str) or (email ==""):
#         return True
#     elif (not '@' in email) or ( not '.com' in email):
#         return True
#     elif not '.com' in email:
#         return True   
#     else: 
#         return False
# a = 'pawarpankaj@gma.com'
def valid_email(email):
   return(True if email==None or not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
   , email) or email=='' else False)


#    return (True if email==None or re.match(r"[^@]+@[^@]+\.[^@]+", email) or email==''else False)
#    return(True if email==None or not re.match(r"[^@]+@[^@]+\.[^@]+", email) or email=='' else False)


a = 'dflk.jpg'

def valid_image (image):
    return (True if not (str(image).endswith(('.jpeg','.jpg','.png','.webp')))else False)
    
print(valid_image(a))


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

