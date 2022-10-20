from django.contrib import admin
from .models import *

class CustomerAdmin(admin.ModelAdmin):
   list_display = ["user", "name", "email"]
   list_filter = ["user"]

admin.site.register(Customer, CustomerAdmin)

class ProductAdmin(admin.ModelAdmin):
   list_display = ["name", "price", "digital"]
   list_filter = ["name"]

admin.site.register(Product, ProductAdmin)

class OrderAdmin(admin.ModelAdmin):
   list_display = ["customer", "order_date", "is_complete", "transaction_id"]
   list_filter = ["customer", "transaction_id"]

admin.site.register(Order, OrderAdmin)

class OrderItemAdmin(admin.ModelAdmin):
   list_display = ["product", "order", "quantity", "add_date"]
   list_filter = ["product"]

admin.site.register(OrderItem, OrderItemAdmin)

class ShippingAddressAdmin(admin.ModelAdmin):
   list_display = ["customer", "order", "address", "city", "zipcode", "add_date"]
   list_filter = ["customer", "order"]

admin.site.register(ShippingAddress, ShippingAddressAdmin)