from core.models import RefModel
from django.db import models


class CategoryModel(RefModel):
    
    class Meta:
        
        verbose_name_plural='دسته بندی'
        verbose_name='دسته بندی'
    
    name = models.CharField(verbose_name="نام دسته بندی", help_text="""""", max_length=100)