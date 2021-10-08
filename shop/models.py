
from functools import total_ordering
from re import T
from django.db import models
from datetime import datetime
from django.db.models import fields
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField

from django.db.models.fields.related import OneToOneField
from users.models import User
from rest_framework import serializers
from users.models import Delivery



def upload_path(instance , filname):
    return '/'.join(['productss' , str(instance.name),filname])
# Create your models here.
class Category(models.Model):
     name = models.CharField(max_length=255, null=True, blank=True)   



class Products(models.Model): 
    
    name = models.CharField(max_length=500,null=True,blank=True )
    image = models.ImageField(null = True ,blank = True , upload_to=upload_path)
    price =models.FloatField( null=True,blank=True)
    description =models.CharField(max_length=500 ,null=True,blank=True)
    date = models.DateTimeField(null=True,blank=True,default=datetime.now())
    numberofvisitors = models.IntegerField(default=0, blank=True)
    categoryId = models.ForeignKey(Category ,null = True,on_delete=models.CASCADE)
    brand = models.CharField(max_length=255 , null = True , blank = True)
    numSales = models.IntegerField(default=0, blank=True)
    providerId = models.IntegerField(default=0, blank=True)
    def __str__(self):
        return  (self.name ,self.categoryId.name)
   

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'

class CetegorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__' 

class order(models.Model):
    delivery=models.IntegerField(null=True, blank=True)
    user = models.ForeignKey(User ,null = True,on_delete=models.CASCADE)
    total = models.FloatField(null = True ,blank=True , default=0 )
    name =models.CharField(max_length=255 , null=True , blank=True)
    email =models.CharField(max_length=255 , null=True , blank=True)
    date= models.CharField(max_length=255 , null=True , blank=True)
    etat= models.CharField(max_length=255 , null=True , blank=True)
    

class orderSerializer(serializers.ModelSerializer):
    class Meta:
        model = order
        fields = '__all__'     

class orderitem(models.Model):
    order = models.ForeignKey(order , null=True , on_delete=models.CASCADE)
    nameprod = models.CharField(max_length=255 , null=True , blank=True)
    qt = models.IntegerField(null=True , blank=True)
    price = models.FloatField(null=True , blank=True)
    prodid = models.IntegerField(null=True , blank=True)

class orderitemSerializer(serializers.ModelSerializer):
    class Meta:
        model = orderitem
        fields = '__all__'        


