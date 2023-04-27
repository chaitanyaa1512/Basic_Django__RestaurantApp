from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('food',views.food, name='food'),
    path('table',views.table, name='table'),
    path('waiter',views.waiter, name='waiter'),
    path('order',views.order, name='order'),
  
    path('Fooddata',views.fooddata),
    path('Tabledata',views.tabledata),
    path('Waiterdata',views.waiterdata),
    path('Orderdata',views.orderdata),
]


