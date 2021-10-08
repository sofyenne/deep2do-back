from django.db import models
from datetime import datetime

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=500,null=True,blank=True )
    lien = models.CharField(max_length=500,null=True,blank=True)
    image = models.CharField(max_length=500 ,null=True,blank=True)
    price =models.FloatField( null=True,blank=True)
    description =models.CharField(max_length=500 ,null=True,blank=True)
    date = models.DateTimeField(null=True,blank=True,default=datetime.now())
    numberofvisitors = models.IntegerField(default=0, blank=True)
    category = models.CharField(max_length=255 , null = True , blank = True)
    brand = models.CharField(max_length=255 , null = True , blank = True)
    officialsite = models.CharField(max_length=500, null=True,blank=True )
    

