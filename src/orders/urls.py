from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    #path('process/', views.order_process, name='order_process'),
    path('create/', views.order_create, name='order_create'),
    path('created/<int:order_id>/', views.order_created, name='order_created'),
    #path('Edit/', views.orders_edit, name='orders_edit'),
    
]


