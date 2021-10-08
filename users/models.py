from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework import serializers





class User(AbstractUser):

    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255 , unique=True)
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    username = None
    
    

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class Delivery(models.Model):
     country = models.CharField(max_length=255 , null=True , blank=True)
     city = models.CharField(max_length=255 , null=True , blank=True)
     place = models.CharField(max_length=255 , null=True , blank=True)
     user=models.ForeignKey(User ,on_delete=models.CASCADE)
     
class deliverySerialize(serializers.ModelSerializer):
    class Meta:
        model = Delivery
        fields = '__all__'