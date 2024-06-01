from core.models import RefModel
from django.db import models


class ItemModel(RefModel):
    
    class Meta:
        
        verbose_name_plural='سفارشات'
        verbose_name='سفارشات'
    
    name = models.CharField(verbose_name="نام", help_text="""""", max_length=100)
    price = models.IntegerField(verbose_name="قیمت", help_text="""""")
    desc = models.TextField(verbose_name="توضیحات", help_text="""""", max_length=None)
    category = models.ForeignKey("main.CategoryModel", verbose_name="دسته بندی", help_text="""""", on_delete=models.CASCADE)
    
    
    def __str__(self):
        return f"{self.name} - ({self.price})"