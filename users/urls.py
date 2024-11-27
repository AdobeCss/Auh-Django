from django.urls import path 
from .views import user_add,user_rem,user_list,user_update

urlpatterns = [
    path('', user_list, name='user_list'),
    path('add', user_add, name='user_add'), 
    path('rem/<int:id>', user_rem, name='user_rem'), 
    path('update/<int:id>', user_update, name='user_update'), 
]