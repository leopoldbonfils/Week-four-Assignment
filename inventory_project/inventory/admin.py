# inventory/admin.py

from django.contrib import admin
from .models import Category, InventoryItem


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display  = ['name', 'description', 'created_at']
    search_fields = ['name']


@admin.register(InventoryItem)
class InventoryItemAdmin(admin.ModelAdmin):
    list_display    = ['name', 'sku', 'category', 'quantity',
                       'unit_price', 'stock_status', 'is_active']
    list_filter     = ['category', 'is_active']
    search_fields   = ['name', 'sku']
    readonly_fields = ['created_at', 'updated_at',
                       'total_value', 'stock_status']
    list_editable   = ['quantity', 'is_active']

    fieldsets = (
        ('Item Info', {
            'fields': ('name', 'sku', 'category', 'description')
        }),
        ('Stock', {
            'fields': ('quantity', 'unit_price', 'total_value', 'stock_status')
        }),
        ('Status & Timestamps', {
            'fields': ('is_active', 'created_at', 'updated_at')
        }),
    )