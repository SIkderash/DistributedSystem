
from cgitb import text
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from .uploader import minioClient
from Story.models import Status
from Story.serializers import StatusSerializer
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
def addStatus(request):
    if request.method=='POST':    
        token = request.COOKIES.get('jwt')
        #print(request.data)
        text = JSONParser().parse(request)['text']
        print(token)
        
        if not token:
            raise AuthenticationFailed('Unauthenticated!')

        else:
            url = 'http://authservice:8000/auth/api_call/'
            #url = 'http://localhost:8000/auth/api_call/'
            data = {'jwt' : token} 
            username = requests.post(url, headers={}, data=data).json()
            print(username)
            uid = str(uuid.uuid4())
            Status.objects.create(uid = uid, username = username, text = text)
            return JsonResponse(str(uid), safe = False)


@csrf_exempt
@api_view(['POST'])
def getFeed(request):
    if request.method=='POST':    
        token = request.COOKIES.get('jwt')
        print(token)
        if not token:
            raise AuthenticationFailed('Unauthenticated!')

        else:
            url = 'http://authservice:8000/auth/api_call/'
            #url = 'http://localhost:8000/auth/api_call/'
            data = {'jwt':token} 
            resp = requests.post(url, headers={}, data=data)
            payload = resp.json()
            print("Payload")
            print(payload)

            #feed = Status.objects.filter(~Q(username=payload))
            feed = Status.objects.all()
            feed = feed[max(len(feed)-10,0):]
            feed = reversed(feed)
            serialized = StatusSerializer(feed, many = True)
            return JsonResponse(serialized.data, safe = False)

        

        
