from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from models.main.category import CategoryModel
from import_export.admin import ImportExportMixin
from import_export import resources, fields
from models.main.item import ItemModel
from models.orders.order import OrderModel, OrderItem
from django.utils.html import mark_safe
from django.shortcuts import render 
from models.orders.person import Person
from django.utils.translation import gettext_lazy as _
import datetime

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


class OrderModelResource(resources.ModelResource):
    price = fields.Field(attribute="_price", column_name="price")

    def after_export(self, queryset, data, *args, **kwargs):
        total = 0
        for order in queryset:
            total += order._price
        data.append([total, f"{queryset.count()} count",  ""])

    class Meta:
        model = OrderModel
        fields = ('id', 'created_at', 'price')


# Custom filter for start time (from)
class StartTimeFilter(admin.SimpleListFilter):
    title = _('از ساعت')
    parameter_name = 'start_hour'

    def lookups(self, request, model_admin):
        # Create options for all 24 hours
        return [(str(hour), f'{hour:02d}:00') for hour in range(24)]

    def queryset(self, request, queryset):
        if self.value() is not None:
            try:
                hour = int(self.value())
                return queryset.filter(created_at__hour__gte=hour)
            except (ValueError, TypeError):
                pass
        return queryset


# Custom filter for end time (to)
class EndTimeFilter(admin.SimpleListFilter):
    title = _('تا ساعت')
    parameter_name = 'end_hour'

    def lookups(self, request, model_admin):
        # Create options for all 24 hours
        return [(str(hour), f'{hour:02d}:59') for hour in range(24)]

    def queryset(self, request, queryset):
        if self.value() is not None:
            try:
                hour = int(self.value())
                # If it's the last hour of the day (23), include all minutes up to 59
                if hour == 23:
                    return queryset.filter(created_at__hour__lte=hour, created_at__minute__lte=59)
                else:
                    return queryset.filter(created_at__hour__lte=hour)
            except (ValueError, TypeError):
                pass
        return queryset


        
@admin.register(OrderModel)
class OrdersPanel(ImportExportMixin, admin.ModelAdmin):
    
    @admin.display(description="پرینت")
    def printFactor(self, obj):
        
        return mark_safe(f"<a href='https://cup-server.liara.run/factor/{obj.pk}' target='_blank'>پرینت فاکتور</a>")
    
    @admin.display(description="سفارشات")
    def ordersItems(self, obj):
        
            
        return ' - '.join([f"{item.item.name} {item.count}" for item in obj.items])
    
    
    @admin.action(description="دانلود لیست روزانه")
    def listOrderCalc(self, request, queryset):
        # ItemModel.objects.filter(pk__in)
        sumPrice = 0
        for order in queryset:
            sumPrice += order._price
                
    inlines = [OrderItemModelInline]
    list_display = ["pk", "status", "person", "desc", "price", "offer", 'printFactor', 'ordersItems']
    list_filter = ['status', "created_at", "person", StartTimeFilter, EndTimeFilter]
    actions = [listOrderCalc]
    resource_classes = [OrderModelResource]

