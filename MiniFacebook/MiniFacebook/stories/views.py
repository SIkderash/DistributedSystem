
from cgitb import text
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from users.serializers import UsersSerializer
from .uploader import minioClient
from stories.models import Status, Stories
from stories.serializers import StatusSerializer, StoriesSerializer
from users.models import Users
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from .uploader import getObjects
from django.db.models import Q
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.decorators import api_view
import jwt, datetime


import uuid

from rest_framework.decorators import api_view

# Create your views here.

@csrf_exempt
@api_view(['POST'])
def addStory(request):
    if request.method=='POST':                                    
        data=JSONParser().parse(request)
        username = data['username']
        uid = str(uuid.uuid4())
        Stories.objects.create(uid = uid, username = username)
        return JsonResponse(str(uid), safe = False)

@api_view(['POST'])
@csrf_exempt
def imageUpload(request):
    print("FILE NAME : " , request.data.get('file_name'))
    minioClient(request.data.get('file_name'), request.FILES['image'])
    return JsonResponse("Photo Uploaded Successfully", safe = False)


@csrf_exempt
@api_view(['POST'])
def addStatus(request):
    if request.method=='POST':                                    
        data=JSONParser().parse(request)
        username = data['username']
        text = data['text']
        uid = str(uuid.uuid4())
        Status.objects.create(uid = uid, username = username, text = text)
        return JsonResponse(str(uid), safe = False)


@csrf_exempt
@api_view(['GET'])
def getStories(request):
    if request.method=='GET':  
        stories = Stories.objects.all()
        serialized = StoriesSerializer(stories, many = True)
        return JsonResponse(serialized.data, safe = False)


@csrf_exempt
@api_view(['POST'])
def getFeed(request):
    if request.method=='POST':    
        token = request.COOKIES.get('jwt')
        print(token)
        if not token:
            raise AuthenticationFailed('Unauthenticated!')

        try:
            payload = jwt.decode(token, 'secret', algorithm=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        print(payload['username'])   
    
        feed = Status.objects.filter(~Q(username=payload['username']))
        #feed = Status.objects.all()
        feed = feed[max(len(feed)-10,0):]
        feed = reversed(feed)
        serialized = StatusSerializer(feed, many = True)
        return JsonResponse(serialized.data, safe = False)


# @csrf_exempt
# @api_view(['POST'])
# def getFeed(request):
#     if request.method=='POST':   
#         data=JSONParser().parse(request)
#         username = data['username']
#         #feed = Status.objects.filter(~Q(username=username))
#         feed = Status.objects.all()
#         feed = feed[max(len(feed)-10,0):]
#         feed = reversed(feed)
#         serialized = StatusSerializer(feed, many = True)
#         return JsonResponse(serialized.data, safe = False)


        
