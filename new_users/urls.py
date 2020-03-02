from django.urls import path
from new_users import views
# from django.conf import settings
# from django.conf.urls.static import static

urlpatterns = [
     path('create_user/', views.create_user)
]