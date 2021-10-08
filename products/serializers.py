from rest_framework import serializers
from .models import Product





class productSerializer(serializers.ModelSerializer):
        class Meta: 
                model = Product 
                fields = '__all__'

        def create(self,validated_data):
                instance = self.Meta.model(**validated_data)
                instance.save()
                return instance 