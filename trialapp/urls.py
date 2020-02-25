from django.urls import path
from trialapp import views

urlpatterns = [
    path('create_store/', views.create_store),
    path('create_product/', views.create_product),
    path('get_store_by_id/', views.get_store_by_id),
    path('get_product_by_id/', views.get_product_by_id),
    path('get_all_store/',views.get_all_store),
    path('get_all_product/',views.get_all_product),
    
]
