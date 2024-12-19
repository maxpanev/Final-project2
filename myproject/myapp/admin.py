from django.contrib import admin
from .models import Product, Order

class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'status', 'created_at']
    list_filter = ['status']
    search_fields = ['user__username', 'phone']

admin.site.register(Product)
admin.site.register(Order, OrderAdmin)