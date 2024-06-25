from django.contrib import admin
from .models import Cart, CartItem
from django.contrib import admin
from parler.admin import TranslatableAdmin

from .models import Product_2, ProductImage

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 0

@admin.register(Product_2)
class Product2Admin(TranslatableAdmin):
    list_display = ('title', 'categories', 'price', 'discount', 'true_price', 'count', 'updated_on')
    list_filter = ('categories', 'updated_on')
    search_fields = ('title', 'description')
    inlines = [ProductImageInline]
    readonly_fields = ('created_on',)

class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 0

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_date', 'modified_date')
    inlines = [CartItemInline]

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'cart', 'quantity', 'is_active', 'created_date', 'modified_date')
    list_filter = ('is_active',)
    search_fields = ('product__name',)