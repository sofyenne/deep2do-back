from django.core.mail.message import EmailMessage
from django.shortcuts import render
from django.template.response import TemplateResponse
from django.urls.conf import path
from rest_framework import status
from rest_framework.views import  APIView 
from rest_framework.response import Response
from .serializers import UserSerializer
from .models import User
from rest_framework.exceptions import AuthenticationFailed
import jwt 
from datetime import datetime, timedelta
from .serializers import ContactSerailizer
from django.core.mail import BadHeaderError, send_mail
from django.http import JsonResponse
import io
from reportlab.pdfgen import canvas


# Create your views here.


class contact(APIView):
    def post(self,request):
      
       
       
        message = request.data['Message']
        email = request.data['email']
    
        # send mail
                            
        if    message: 
            try:
                email = EmailMessage('Contact Admin ', message,'deep2dosofien@gmail.com',['sofienayari.130@gmail.com'] , )
                
                email.send()
            except BadHeaderError:
                     msg='invalid header found'
                     return Response({'respense':msg})
           
            return  Response({'respense':'success sendig mail'})      
        else:
            msg = 'Make sure all fields are entered and valid.'
            return Response({'respense':msg})  

class register(APIView):
   def post(self,request):
       serializer = UserSerializer(data=request.data)
       serializer.is_valid(raise_exception=True)
       serializer.save()
       return Response(serializer.data)


class login(APIView):
    def post(self , request):
        email = request.data['email']
        password= request.data['password']

        user =User.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed('User not found')
       
        if not user.check_password(password) :
            raise AuthenticationFailed('Incorrect password')
        
        payload = {
          'id' : user.id,
          'exp' : datetime.utcnow() + timedelta(minutes=60),
          'iat' :datetime.utcnow()
        }

        token = jwt.encode(payload , 'secret' , algorithm = 'HS256').decode('utf-8')

        response = Response()

        response.set_cookie(key = 'jwt' , value = token , httponly = True)

        response.data={
            'jwt' :token
        }


        return response         


class getuser(APIView):
    def get(self , request):
        token=request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed('Unitentificate')
        try:
            pyload = jwt.decode(token , 'secret', algorithm=['HS256'])
        except jwt.ExpiredSignature:
            raise AuthenticationFailed('Unitentificate')    

        user = User.objects.filter(id =pyload['id']).first()
        serializer = UserSerializer(user)

        return Response(serializer.data) 


class logout(APIView):
    def post(self , request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {

            'message' : 'success'
        }
        return response


class usercrud(APIView) : 


    def put(self , request , pk):
        savedobj = User.objects.get(pk=pk)
        data = request.data
        serializer = UserSerializer(instance=savedobj , data = data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self , request , pk):
        obj = User.objects.get(pk=pk)
        obj.delete()
        return Response(status=status.HTTP_200_OK)

    def get(self , request ,pk) :

        user = User.objects.get(pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

class alluser(APIView):
    def get(self , request):
        obj = User.objects.all()
        serializer = UserSerializer(obj , many=True)
        return Response(serializer.data)
        
                


