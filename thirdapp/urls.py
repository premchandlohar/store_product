from django.urls import path
from thirdapp import views

urlpatterns = [
    path('create_person/',views.create_person),
    path('create_group/',views.create_group),
    
    
    
]