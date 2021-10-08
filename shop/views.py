from users.models import deliverySerialize
from django import http
from django.http.response import HttpResponse
from rest_framework import response
from rest_framework.response import Response
from shop.models import ProductSerializer
from django.shortcuts import render
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.generics import UpdateAPIView
from .models import *
import json
from django.http import JsonResponse
from rest_framework import status

# Create your views here.




class Getallproduct(APIView):
    def get(self , request):
        productlist = Products.objects.all()
        serializer = ProductSerializer(productlist , many = True)
        return Response(serializer.data)
    def post(self , request):
        serobj = ProductSerializer(data=request.data)  
        if serobj.is_valid(raise_exception=True) :
            serobj.save()
            return Response(serobj.data)
        return Response(serobj.error_messages)      

class getallcategory(APIView):
    def get(self , request):
        categoryList = Category.objects.all()
        serializer = CetegorySerializer(categoryList, many=True)  
        return Response(serializer.data)     
class favorite(APIView):
     def put(self,request, pk):
        prod=Products.objects.get(pk=pk)
        if prod is not None :
            if prod.numberofvisitors == 0  :
                  prod.numberofvisitors=request.data['user']
                  prod.save()
                  res = Response()
                  res.data = {
                     'message' : 'product favored'
                  }
                  return res
            else :
                 prod.numberofvisitors = 0
                 prod.save()
                 res = Response()
                 res.data = {
                     'message' : 'product delete off favorites list'
                 }
                 return res

        return Response(status)

class actionProdByid(APIView):
    def get(self,request, pk):
        prod=Products.objects.get(pk=pk) 
        ser = ProductSerializer(prod)       
        return Response(ser.data)
    def delete(self,request, pk):
         prod=Products.objects.get(pk=pk)
         prod.delete()
         return Response(status=status.HTTP_200_OK)
    def put(self,request, pk):
        prod=Products.objects.get(pk=pk)
        serializer = ProductSerializer(prod,data=request.data)  
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class getnewlyadd(APIView):
    def get(self , request):
        prod = Products.objects.all().order_by('-date')
        ser = ProductSerializer(prod , many = True)
        return Response(ser.data)

class getselling(APIView):
    def get(self , request):
        prod = Products.objects.all().order_by('-numSales')
        ser = ProductSerializer(prod, many = True)
        return Response(ser.data)
        
class getbycategory(APIView):
    def get(self , request, id):
        prod = Products.objects.all().filter(categoryId=id)
        ser = ProductSerializer(prod , many = True)
        return Response(ser.data)        
#______________________________________________________crude order_____________________________________________________#

class creatorder(APIView):
    def post(self , request):
        serializer = orderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class getorder(APIView):
    def get(self , request , pk):
        serializer = order.objects.filter(user_id= pk ).last()
        ser = orderSerializer(serializer )
        return Response(ser.data)
class getandupdateorder(APIView):
    def get(self , request , pk ):
        obj = order.objects.get(pk=pk)
        ser = orderSerializer(obj)
        return Response(ser.data)
    def put(self , request , pk ) :
         obj = order.objects.get(pk=pk)
         if obj is not None :
                  obj.etat='confirmed'
                  obj.save()
                  return Response(status=status.HTTP_200_OK)
         return Response(status=status.HTTP_304_NOT_MODIFIED)   
    def delete(self, request, pk, format=None):
        obj = order.objects.get(pk=pk)
        obj.delete()
        res = Response()
        res.data={'message' : 'order deleted'}
        return res

class cancelorder(APIView):
         def put(self , request , pk ) :

              obj = order.objects.get(pk=pk)
              if obj is not None :

                  obj.etat='cancled'
                  obj.save()
                  res=Response()
                  res.data={'message':'order cancled'}
                  return res
              return Response(status=status.HTTP_304_NOT_MODIFIED)            
class getallorder(APIView):
    def get(self , request):
        serializer = order.objects.all()
        ser = orderSerializer(serializer,many=True )
        return Response(ser.data)

@api_view(['GET']) 
def getAllorderbyUser(request,pk):
    ord= order.objects.prefetch_related('orderitem_set').all().filter(user_id=pk)
    ser = orderSerializer(ord,many=True )
    return JsonResponse(ser.data , safe=False)      
#-------------------------------------------------------crude orderitem-------------------------#
@api_view(['GET']) 
def getAllitem(request):
    ord= orderitem.objects.all()
    ser = orderitemSerializer(ord , many= True)
    return Response(ser.data)      
@api_view(['GET']) 
def orderitemById(request , id):
    ord= orderitem.objects.all().filter(order=id)
    ser = orderitemSerializer(ord , many= True)
    return Response(ser.data)      

@api_view(['POST'])
def createall(request):
    listdata= request.data['orderitem']
    for i in listdata:
        item = orderitemSerializer(data =i)
        item.is_valid(raise_exception=True)
        item.save()
    return Response(listdata)
#--------------------------------------------------------------cuder catégory----------------------------------#
class getandcreatecategory(APIView):
    def post(self,request):
        serializer = CetegorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    def get(self ,request):
         serializer =Category.objects.all()
         ser = CetegorySerializer(serializer,many=True )
         return Response(ser.data)
class deletcategory(APIView):
    def delete(self, request, pk, format=None):
        snippet = Category.objects.get(pk=pk)
        snippet.delete()
        return Response("done")     
class UpdatecategoryAPIView(UpdateAPIView):
    """This endpoint allows for updating a specific todo by passing in the id of the todo to update"""
    queryset = Category.objects.all()
    serializer_class = CetegorySerializer

#----------------------------------------------------------------------------------------------------
#        
class delivery(APIView):
    def post(self , request):
        serializer = deliverySerialize(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status)
    def get(self , request):
        obj = Delivery.objects.all()
        ser = deliverySerialize(obj , many=True)
        return Response(ser.data)        
class deliverbyId(APIView):
    def get(self, request , pk ):
        obj = Delivery.objects.all().filter(user=pk)
        if obj is not None:
             ser = deliverySerialize(obj , many=True)
             return Response(ser.data)
        return Response(status=status.HTTP_404_NOT_FOUND)    

    def delete(self , request , pk):
        obj = Delivery.objects.get(pk=pk)
        if obj is not None : 
            obj.delete()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status)         

@api_view(['GET']) 
def getAdressebyOrder(request , id):
    ord= Delivery.objects.get(pk=id)
    ser = deliverySerialize(ord)
    return Response(ser.data)       