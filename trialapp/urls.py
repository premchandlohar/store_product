from django.urls import path
from trialapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('create_store/', views.create_store),
    path('create_category/', views.create_category),
    path('create_subcategory/', views.create_subcategory),
    path('create_product/', views.create_product),
    path('get_store_by_id/', views.get_store_by_id),
    path('get_category_by_id/', views.get_category_by_id),
    path('get_subcategory_by_id/', views.get_subcategory_by_id),
    path('get_product_by_id/', views.get_product_by_id),
    path('get_all_store/',views.get_all_store),
    path('get_all_category/',views.get_all_category),
    path('get_all_subcategory/',views.get_all_subcategory),
    path('get_all_product/',views.get_all_product),
    path('get_category_by_store_id/',views.get_category_by_store_id),
    path('get_subcategory_by_category_id/',views.get_subcategory_by_category_id),
    path('get_products_by_store_id/',views.get_products_by_store_id),
    path('update_store_by_field/',views.update_store_by_field),
    path('update_category_by_field/',views.update_category_by_field),
    path('update_subcategory_by_field/',views.update_subcategory_by_field),
    path('update_product_by_field/',views.update_product_by_field),
    path('delete_store_by_id/',views.delete_store_by_id),
    path('delete_category_by_id/',views.delete_category_by_id),
    path('delete_subcategory_by_id/',views.delete_subcategory_by_id),
    path('delete_product_by_id/',views.delete_product_by_id),
    path('create_followership/',views.create_followership),


    # path('update_store_by_id/',views.update_store_by_id),
    # path('update_product_by_id/',views.update_product_by_id),
    # path('update_product_by_store_id/',views.update_product_by_store_id),
    # path('update_or_create_product_by_id/',views.update_or_create_product_by_id),
    # path('get_or_create_store_by_id/',views.get_or_create_store_by_id),
    # path('get_or_create_product_by_id/',views.get_or_create_product_by_id),



]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
