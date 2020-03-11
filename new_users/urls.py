from django.urls import path
from new_users import views

urlpatterns = [
     path('create_user/', views.create_user),
     path('get_user_by_id/', views.get_user_by_id),
     path('get_all_users/', views.get_all_users),
     path('update_user_by_field/', views.update_user_by_field),
     path('create_address/', views.create_address),
     path('update_address_by_address_id/', views.update_address_by_address_id),
     path('get_address_by_id/', views.get_address_by_id),
     path('get_all_address/', views.get_all_address),
     path('delete_user_by_id/', views.delete_user_by_id),
     path('delete_address_by_id/', views.delete_address_by_id),
     path('get_addresses_of_user/', views.get_addresses_of_user),
     # path('create_relationship/', views.create_relationship),


]


