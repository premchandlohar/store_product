from django.urls import path
from thirdapp import views

urlpatterns = [
    path('create_person/',views.create_person),
    path('create_group/',views.create_group),
    path('get_person/',views.get_person),
    path('get_group/',views.get_group),
    path('create_membership/',views.create_membership),
    path('get_membership/',views.get_membership),
    
    
    
]