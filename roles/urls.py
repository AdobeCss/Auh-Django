from django.urls import path 
from .views import role_list

urlpatterns = [
    path('', role_list, name='role_list')
]