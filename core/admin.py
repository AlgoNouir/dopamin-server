from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from models.main.category import CategoryModel
from import_export.admin import ImportExportMixin
from models.main.item import ItemModel
from models.orders.order import OrderModel, OrderItem
from django.utils.html import mark_safe
from django.shortcuts import render 



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
        
        return mark_safe("<button onClick={window.print()}>پرینت فاکتور</button>")
    
    @admin.display(description="سفارشات")
    def ordersItems(self, obj):
        
            
        return ' - '.join([f"{item.item.name} {item.count}" for item in obj.items])
    
    inlines = [OrderItemModelInline]
    list_display = ["pk", "status", "desc", "price", 'printFactor', 'ordersItems']
    list_filter = ['status']