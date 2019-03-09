from django.db import models
from enum import unique


class Book(models.Model):
    nid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32)
    pub_date = models.DateField(blank=True,null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2,blank=True,null=True)
    # 与Publish建立一对多的关系，外键字段建立在多的一方
#     publish = models.ForeignKey(to="Publish",to_field='nid',on_delete=models.CASCADE)
    # 与Author表建立多对多的关系，ManyToManyField
#    authors = models.ManyToManyField(to='Author',)
    publish = models.CharField(max_length=100,blank=True)
    authors_name = models.CharField(max_length=32,blank=True)
    link = models.URLField(max_length=300,blank=True)
    
class FirLibAdmin(models.Model):
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=256)
    
