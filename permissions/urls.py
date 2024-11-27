from django.urls import path 
from .views import permissions_add,permissions_rem,permissions_list,permissions_update

urlpatterns = [
    path('', permissions_list, name='permissions_list'),
    path('add', permissions_add, name='permissions_add'), 
    path('rem/<int:id>', permissions_rem, name='permissions_rem'), 
    path('update/<int:id>', permissions_update, name='permissions_update'), 
]