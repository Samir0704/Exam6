from django.contrib import admin # type: ignore
from django.urls import path # type: ignore

from blog.views import index,detail_product,add_comment,customer_details,customer_list,delete_customer,customer_edit
from blog.models import Customer 
urlpatterns = [
    path('', index, name='index'),
    path('detail/<int:pk>', detail_product, name='detail_product'),
    path('detail/<int:product_id>/comment', add_comment, name='add_comment'),
    path('custumers/<int:pk>',customer_details,name='customer_details'),
    path('customer/', customer_list, name='customer_list'),
    path('customer/<int:pk>/', delete_customer, name='delete_customer'),
    path('customer/<int:pk>/', customer_edit, name='customer_edit')
]
