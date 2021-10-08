from django.http import response
from django.shortcuts import render
from rest_framework.views import  APIView 
from rest_framework.response import Response
from .models import Product
from .serializers import productSerializer
import json
from datetime import datetime


# Create your views here.


class getlastvisited(APIView):
  def get(self , request):
    listprod = Product.objects.all().order_by('date').reverse()
    serializer = productSerializer(listprod , many = True)
    return Response(serializer.data)


class getproduct(APIView):
  def get(self,request):
    listprod = Product.objects.all().order_by('price')
    seralizer = productSerializer(listprod , many=True)
    return Response(seralizer.data)
    
class getproductvisited(APIView):
  def get(self , request):
    listvisited = Product.objects.all().order_by('numberofvisitors').reverse()
    seralizer = productSerializer(listvisited , many=True)
    return Response(seralizer.data)


class createproduct(APIView):

  def post(self , request):
    name = request.data['name']
    prod= Product.objects.filter(name = name).first()
    if prod is None:
      serializer = productSerializer(data=request.data)
      serializer.is_valid(raise_exception=True)
      serializer.save()
      message = 'product saved'
      return Response({"message" : message})
    else : 
         prod.numberofvisitors = prod.numberofvisitors + 1 
         prod.date = datetime.now()
         prod.save() 
         msg ='product updated' 
         return Response({"message" : msg})

class search(APIView):
     def post(self,request):
         data = request.data['search']
         
         productpotentiallabs = crawlpotentiallabs(data)
         productiotasia = crawliotasia(data)
         productrobocraze = robocraze(data)
         listproduct = []
         for i in productpotentiallabs:
           listproduct.append(i)
         for j in productiotasia : 
           listproduct.append(j)

         for k in productrobocraze:
           listproduct.append(k)     
 
         return Response(listproduct)

         
     



def crawlpotentiallabs(search):

  from bs4 import BeautifulSoup as bs
  import requests
  produit = []
  search = search.replace(" " ,"%20")
  url ="https://potentiallabs.com/cart/index.php?route=product/search&search="+search
  r=requests.get(url)

  soup=bs(r.content)
  bloc = soup.find_all("div" , attrs={"class":"row main-products product-grid"})

  for i in bloc:

    prod = i.find_all("div" , attrs={"class" :"product-grid-item xs-50 sm-33 md-33 lg-25 xl-20"})
  
    for item in prod :

      products={}
      products['officialsite'] = 'potentiallabs'
      products['image'] = item.find("div" ,  attrs={"class" :"image"}).a.img['src']
    
      products['lien'] = item.find("div" , attrs={"class" : "product-details"}).div.h4.a['href']
    
      products['name'] = item.find("div" , attrs={"class" : "product-details"}).div.h4.a.text.strip()
    
      prix = item.find("p",  attrs = {"class" : "price"}).text.strip()
      products['price'] = prix.replace(" " , "")

      produit.append(products)
  return produit    




def crawliotasia(search):

  from bs4 import BeautifulSoup as bs
  import requests
  produit = []
  search = search.replace(" " ,"+")
  url ="https://www.iotasia.online/search?q="+search
  r=requests.get(url)

  soup=bs(r.content)
  bloc = soup.find_all("div" , attrs={"class" : "grid__item large--four-fifths"})

  for i in bloc:

    prod = i.find_all("div" , attrs={"class" :"grid"})
  
    for item in prod :

      products={}
      products['officialsite'] = 'iotasia'
      products['image'] = item.div.a.img['src']
    
      lien = item.find("div" , attrs={"class" : "grid__item one-fifth"}).a['href']

      products['lien']='https://www.iotasia.online/'+lien
    
      products['name'] = item.find("div" , attrs={"class" : "grid__item four-fifths"}).h3.a.text.strip()
    
      prix = item.find("div" , attrs={"class" : "grid__item four-fifths"}).span.span.text.strip()
      products['price'] = prix[1:].replace(" " , "")

      products['desc'] = item.find("div" , attrs={"class" : "grid__item four-fifths"}).p.text.strip()

      produit.append(products)
  return produit   


def robocraze(search):

  from bs4 import BeautifulSoup as bs
  import requests
  produit = []
  src = ""
  search = search.replace(" " ,"+")
  url ="https://robocraze.com/search?q="+search
  r=requests.get(url)

  soup=bs(r.content)
  bloc = soup.find_all("li" , attrs={"class" :"grid__item one-quarter"})

  for i in bloc:

    prod = i.find_all("div" , attrs={"class" : "card"})
  
    for item in prod :

      products={}
      products['officialsite'] = 'robocraze'
      lien = item.find("a" ,attrs={"class" : "grid-view-item__link grid-view-item__image-container"})['href']
      products['lien']='https://robocraze.com/'+lien
      products['image'] = item.find("div" ,attrs={"class" : "product-card__image-with-placeholder-wrapper"}).div['data-wlh-image']
      products['price'] = item.find("div" ,attrs={"class" : "product-card__image-with-placeholder-wrapper"}).div['data-wlh-price']
      products['name'] = item.find("div" ,attrs={"class" : "product-card__image-with-placeholder-wrapper"}).div['data-wlh-name']
      

      produit.append(products)
  return produit   


def theiotmarketplace(search):

  from bs4 import BeautifulSoup as bs
  import requests
  produit = []
 
  search = search.replace(" " ,"+")
  url ="https://www.the-iot-marketplace.com/search?controller=search&s="+search
  r=requests.get(url)

  soup=bs(r.content)
  bloc = soup.find_all("div" , attrs={"class" :"js-product-miniature-wrapper col-xl-4 col-lg-4 col-sm-6 col-12"})

  for i in bloc:

    prod = i.find_all("article" , attrs={"class" : "product-miniature product-miniature-default product-miniature-grid product-miniature-layout-1 js-product-miniature"})
  
    for item in prod :

      products={}
      products['lien'] = item.find("h3" ,attrs={"class" : "h3 product-title"}).a['href']
      
      products['officialsite'] = 'theiotmarketplace'
      products['name'] = item.find("h3" ,attrs={"class" : "h3 product-title"}).a.text
      price = item.find("span" ,attrs={"class" : "product-price"})
      price = str(price)
      price = price[44:-10]
      products['price']=price
      products['image'] = item.find("img")['data-src']
 
      
     
    
  
      produit.append(products)
  return produit   



