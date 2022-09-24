from django.shortcuts import render

# Create your views here.

from cgitb import text
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from .uploader import minioClient
from Story.models import Stories
from Story.serializers import StoriesSerializer
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from .uploader import getObjects
from django.db.models import Q
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.decorators import api_view
import requests


import uuid

from rest_framework.decorators import api_view

# Create your views here.

@csrf_exempt
@api_view(['POST'])
def addStory(request):
    if request.method=='POST':    
        token = request.COOKIES.get('jwt')
        #print(request.data)
        print(token)
        if not token:
            raise AuthenticationFailed('Unauthenticated!')

        else:
            url = 'http://localhost/auth/api_call/'
            data = {'jwt' : token} 
            username = requests.post(url, headers={}, data=data).json()
            print(username)
            uid = str(uuid.uuid4())
            Stories.objects.create(uid = uid, username = username)
            img = request.FILES['image']
            minioClient(uid, img)
            return JsonResponse("Photo Uploaded Successfully", safe = False)



@csrf_exempt
@api_view(['GET'])
def getStories(request):
    if request.method=='GET':    
        token = request.COOKIES.get('jwt')
        print(token)
        if not token:
            raise AuthenticationFailed('Unauthenticated!')

        else:
            url = 'http://localhost/auth/api_call/'
            data = {'jwt':token} 
            resp = requests.post(url, headers={}, data=data)
            payload = resp.json()
            print("Payload")
            print(payload)
  
            stories = Stories.objects.all()
            stories = stories[max(len(stories)-3,0):]
            stories = reversed(stories)
            serialized = StoriesSerializer(stories, many = True)
            return JsonResponse(serialized.data, safe = False)



        
