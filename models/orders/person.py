from django.db import models



class Person(models.Model):
    
    name = models.CharField("نام مشتری", max_length=100)
    