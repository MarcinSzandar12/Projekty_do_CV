from django.urls import path
from .views import *

app_name="store"
urlpatterns = [
    path('', store, name="store"),
    path('cart/', cart, name="cart"),
    path('checkout/', checkout, name="checkout"),
    path('update_item/', updateItem, name="update_item"),
    path('cart/update_item/', updateItem, name="cart_update_item"),
    path('process_order/', processOrder, name="process_order"),
    path('checkout/process_order/', processOrder, name="checkout_process_order"),
    path('details/<int:id>', productDetails, name="product_details"),
    path('details/update_item/', updateItem, name="details_update_item"),
    
]