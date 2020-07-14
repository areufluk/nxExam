from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from cryptography.fernet import Fernet
from rest_framework import status

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



  
