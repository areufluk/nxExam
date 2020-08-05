from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from cryptography.fernet import Fernet
from rest_framework import status
import pyrebase
import random
import string

key = Fernet.generate_key()
cipher = Fernet(key)

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

#api
@api_view(['POST'])
def reqToken(request):
  if request.method == 'POST': 
    res = {}
    res['type'] = mail_validate(request.data['obj']['email'])
    res['user_token'] = request.data['obj']['id']  
    return Response(res, status = status.HTTP_200_OK)

@api_view(['POST'])
def saveSubject(request):
  if request.method == 'POST':  
    uid = idGen()
    print(request.data)
    print(uid)
    database.child("Exam").child(uid).set(request.data['ex'])
    database.child("Teacher").child(request.data['created_by']).child(uid).set(uid)
    return Response(status = status.HTTP_200_OK)
  return Response(status= status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def updateSubject(request):
  if request.method == 'POST':
    result = database.child("Exam").child(request.data['uid']).update(request.data['update'])
    print(result)
  return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def getSubject(request):
  if request.method == 'GET':
    result = database.child("Exam").child(request.data['uid']).get()
    result = dict(result.val())
    result['uid'] = request.data['uid']
    return Response(result, status=status.HTTP_200_OK)
  return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def getSublist(request):
  exam = {}
  if request.method == 'GET' and database.child('Teacher').child(request.GET['name']).shallow().get().val():
    print(request.GET['name'])
    result = database.child("Teacher").child(request.GET['name']).get()
    for uid in result.each():
      test = form_subject(uid.key())
      exam[uid.key()] = test
  return Response(exam, status=status.HTTP_200_OK)


#help function
def form_subject(uid):
  exam = {}
  exam["subject_name"] = database.child("Exam").child(uid).child("subject_name").get().val()
  exam["subject_id"] = database.child("Exam").child(uid).child("subject_id").get().val()
  exam["teacher_name"] = database.child("Exam").child(uid).child("teacher_name").get().val()
  exam["start_time"] = database.child("Exam").child(uid).child("start_time").get().val()
  exam["end_time"] = database.child("Exam").child(uid).child("end_time").get().val()
  print(exam)
  return exam

def mail_validate(mail):
  gmail = mail.split('@')
  status = 3 #other
  if gmail[1] == 'kmitl.ac.th':
    if gmail[0][0] >= '0' and gmail[0][0] <= '9':
      status = 2 #student
    else:
      status = 1 #teacher
  return status

def idGen(): 
  id_text = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(6)])
  return id_text  
