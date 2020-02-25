from django.urls import path
from trialapp import views

urlpatterns = [
    path('create_store/', views.create_store),
]
