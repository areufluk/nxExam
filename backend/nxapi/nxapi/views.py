from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from cryptography.fernet import Fernet
from rest_framework import status
import pyrebase

config = {
    "apiKey": "AIzaSyBX-GNsgJlhNdYZPXPCSp0oxXuTNTWc49M",
    "authDomain": "nxexam.firebaseapp.com",
    "databaseURL": "https://nxexam.firebaseio.com",
    "projectId": "nxexam",
    "storageBucket": "nxexam.appspot.com",
    "messagingSenderId": "324791212286",
    "appId": "1:324791212286:web:fc6b6e56880d1564792daf",
    "measurementId": "G-KCR57KDFJQ"
}

firebase = pyrebase.initialize_app(config)
database=firebase.database()

@api_view(['POST'])
def reqToken(request):
  if request.method == 'POST':
    print(request.data['obj']['email'])
    user_token = mail_validate(request.data['obj']['email'])  
    return Response(user_token, status = status.HTTP_200_OK)

def mail_validate(mail):
  gmail = mail.split('@')
  status = 300 #other
  if gmail[1] == 'kmitl.ac.th':
    if gmail[0][0] >= '0' and gmail[0][0] <= '9':
      status = 200 #student
    else:
      status = 100 #teacher
  return status 

@api_view(['GET'])
def add(request):
    if request.method == 'GET':
        data = {"title": "Test", "content": "add to database testing" }
        database.child("fluk").child().child("data").push(data)
    return Response(status = status.HTTP_200_OK)



  
