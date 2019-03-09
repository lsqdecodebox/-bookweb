from django.db import models

# Create your models here.

class LibNews(models.Model):
    title= models.CharField(max_length=100)
    link = models.URLField(max_length=300)