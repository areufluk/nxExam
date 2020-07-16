from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from cryptography.fernet import Fernet
from rest_framework import status

from .models_insert import createSubModel
from .serialization import createSubSerialize

from .models_insert_prob import createProbModel
from .serialization import createProbSerialize

from .serialization import serializationClass
from .models import subModel

key = Fernet.generate_key()
cipher = Fernet(key)

@api_view(['POST'])
def reqToken(request):
  if request.method == 'POST':
    print(request.data)
    user_token = mail_validate(request.data['gmail'])  
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
def showSub(request):
    if request.method == 'GET' :
        results = subModel.objects.all()
        serialize = serializationClass(results, many = True)
        return Response(serialize.data)

@api_view(['POST'])
def saveSub(request):
    if request.method == 'POST':
        saveSerialize = createSubSerialize(data=request.data)
        if saveSerialize.is_valid():
            saveSerialize.save()
            return Response(saveSerialize.data, status = status.HTTP_201_CREATED)
            return Response(saveSerialize.data, status = status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def saveProb(request):
    if request.method == 'POST':
        saveSerialize = createProbSerialize(data=request.data)
        if saveSerialize.is_valid():
            saveSerialize.save()
            return Response(saveSerialize.data, status = status.HTTP_201_CREATED)
            return Response(saveSerialize.data, status = status.HTTP_400_BAD_REQUEST)


  
