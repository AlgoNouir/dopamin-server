import enum
from django.contrib import admin
from core.models import RefModel
from django.db import models
from models.main.item import ItemModel
from django.http import FileResponse
from models.orders.person import Person
    
    
class OrderItem(RefModel):
    
    class Meta:
        
        verbose_name_plural='موارد سفارشات'
        verbose_name='موارد سفارش'
        
    
    parent = models.ForeignKey("orders.OrderModel", on_delete=models.CASCADE, verbose_name="سفارش والد")
    item = models.ForeignKey(ItemModel, on_delete=models.CASCADE, verbose_name="منوی سفارش داده شده")
    count = models.IntegerField("تعداد", default=1)
    
    @property
    def price(self):
        return "{:,}".format(self.item.price*self.count)
    
    
    @property
    def itemPrice(self):
        return "{:,}".format(self.item.price)
    
    def __str__(self):
        return f"{self.parent} - {self.item} - {self.count} عدد"
    
    
class OrderStatus(models.IntegerChoices):
    
    PENDING = 1, "در حال تحویل"
    SENDED = 2, "تحویل داده شده"
    DONE = 3, "پرداخت شده"

class OrderModel(RefModel):
    
    class Meta:
        
        verbose_name_plural='سفارشات'
        verbose_name='سفارش'
    
    status = models.IntegerField(verbose_name="تحویل داده شده", choices=OrderStatus.choices, default=OrderStatus.PENDING)
    desc = models.TextField("توضیحات", null=True, blank=True, max_length=10000)
    person = models.ForeignKey(Person, verbose_name="مشتری", null=True, blank=True, on_delete=models.CASCADE)
    
    @admin.display(description="قیمت سفارش (تومان)")
    def price(self):
        price = 0
        for item in OrderItem.objects.filter(parent_id=self.pk):
            price += int(item.item.price) * item.count 
        return "{:,}".format(price)
    
    
    def __str__(self):
        return f"سفارش {self.pk}"
    
    
    @property
    def items(self):
        return OrderItem.objects.filter(parent_id=self.pk)
    