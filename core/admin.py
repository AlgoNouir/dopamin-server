from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from models.main.category import CategoryModel
from import_export.admin import ImportExportMixin
from models.main.item import ItemModel
from models.orders.order import OrderModel, OrderItem


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
    
    inlines = [OrderItemModelInline]
    list_display = ["pk", "status", "desc", "price"]
    list_filter = ['status']