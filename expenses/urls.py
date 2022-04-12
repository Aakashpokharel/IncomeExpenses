import imp
from multiprocessing.spawn import import_main_path
from django.urls import path
from .views import index , add_expenses

urlpatterns = [
    path('',index , name='home'),
    path('add-expenses',add_expenses,name = 'add-expenses',)
]
