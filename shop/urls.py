from django.urls import path
from rest_framework import views 
from .views import *
from .import views



urlpatterns = [
    
    path('prod' , Getallproduct.as_view()),
    path('cancel/<int:pk>' , cancelorder.as_view()),
    path('favorite/<int:pk>' ,favorite.as_view()),
    path('deliveryByOrder/<int:id>' , views.getAdressebyOrder),
    path('orderGA/<int:pk>' , getandupdateorder.as_view()),
    path('allcategory' ,getallcategory .as_view()),
    path('prod/<int:pk>' , actionProdByid.as_view() ),
    path('newly' , getnewlyadd.as_view() ),
    path('selling' , getselling.as_view() ),
    path('prodbycat/<int:id>' , getbycategory.as_view() ),
    path('order/<int:pk>' ,getorder.as_view()),
    path('orderall/<int:pk>' , views.getAllorderbyUser , name="allorderByuser" ),
    path('createorder/' , creatorder.as_view() ),
    path('allitem' , views.getAllitem, name="allitemOrder" ),
    path('allitemById/<int:id>' , views.orderitemById) ,
    path('createitem/' , views.createall , name="createAllItem" ),
    path('getallorder/' ,getallorder.as_view() ),
    path('category/' ,getandcreatecategory().as_view() ),
    path('category/<int:pk>' ,deletcategory().as_view() ),
    path('category/update/<int:pk>' ,UpdatecategoryAPIView().as_view() ),
    path('delivery/' ,delivery().as_view() ),
    path('delivery/<int:pk>' ,deliverbyId().as_view() ),
]