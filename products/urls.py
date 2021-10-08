from .views import search
from .views import createproduct
from .views import getproduct
from .views import getproductvisited
from django.urls import path 
from .views import getlastvisited



urlpatterns = [
    
    path('search' , search.as_view()),
    path('add' , createproduct.as_view()),
    path('get' , getproduct.as_view()),
    path('visited' , getproductvisited.as_view()),
    path('lastvisited' , getlastvisited.as_view()),
   
    
    
]