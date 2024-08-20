from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from models.main.category import CategoryModel
from import_export.admin import ImportExportMixin
from models.main.item import ItemModel
from models.orders.order import OrderModel, OrderItem
from django.utils.html import mark_safe
from django.shortcuts import render 
from models.orders.person import Person


@admin.register(Person)
class PersonPanel(ImportExportMixin, admin.ModelAdmin):
    
    list_display = ['pk', 'name']
    list_filter=[]
    

# --------------------------------------------------------- category


class ItemModelCategoryModelInline(admin.StackedInline):
    model = ItemModel

@admin.register(CategoryModel)
class CategoryPanel(ImportExportMixin, admin.ModelAdmin):
    
    inlines = [ItemModelCategoryModelInline]
    list_display = ['pk', 'name']
    list_filter=[]
    

# --------------------------------------------------------- order

class OrderItemModelInline(admin.TabularInline):
    model = OrderItem

@admin.register(OrderModel)
class OrdersPanel(ImportExportMixin, admin.ModelAdmin):
    
    @admin.display(description="پرینت")
    def printFactor(self, obj):
        
        return mark_safe(f"<a href='http://localhost:8000/factor/{obj.pk}' target='_blank'>پرینت فاکتور</a>")
    
    @admin.display(description="سفارشات")
    def ordersItems(self, obj):
        
            
        return ' - '.join([f"{item.item.name} {item.count}" for item in obj.items])
    
    inlines = [OrderItemModelInline]
    list_display = ["pk", "status", "person", "desc", "price", 'printFactor', 'ordersItems']
    list_filter = ['status', "created_at", "person"]