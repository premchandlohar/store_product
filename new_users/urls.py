from django.urls import path
from new_users import views
# from django.conf import settings
# from django.conf.urls.static import static

urlpatterns = [
     path('create_user/', views.create_user),
     path('get_user_by_id/', views.get_user_by_id),
     path('get_all_users/', views.get_all_users),
     path('update_user_by_field/', views.update_user_by_field),
     path('create_address/', views.create_address),
     path('update_address_by_address_id/', views.update_address_by_address_id),




]
