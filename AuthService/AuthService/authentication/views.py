
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from authentication.models import Users
from authentication.serializers import UsersSerializer
from django.contrib.auth.hashers import make_password, check_password
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 

import uuid
from django.conf import settings
from django.core.mail import send_mail

from rest_framework.decorators import api_view
import jwt, datetime

# Create your views here.
@csrf_exempt
def register(request,id=0):
    if request.method=='POST':                                    #register
        users_data=JSONParser().parse(request)

        username = users_data['username']
        email = users_data['email']
        password = users_data['password']
        uid = str(uuid.uuid4())

        #print(password)
        
        hashed_password = make_password(password)

        user = Users.objects.filter(username=username).first()
        if user is not None:
            return JsonResponse("Username already exists!", safe = False)
        
        user = Users.objects.filter(email=email).first()
        if user is not None:
            return JsonResponse("This email already has a registered account associated with!", safe = False)
        
        Users.objects.create(uid= uid, email = email, username=username, password=hashed_password, isVerified = True)

        #sendMail(email, uid)
        #return JsonResponse("Please check your mail to verify your account", safe=False)
        return JsonResponse("Registration Successful", safe=False)

@csrf_exempt
def sendMail(email_to, uid):
    subject = 'Verify your account'
    body = 'Please click the link to verify your account http://127.0.0.1:8000/verify/' + uid
    email_from = settings.EMAIL_HOST_USER
    recipient = [email_to]
    send_mail(subject, body , email_from, recipient)
    print("mail sent")

@csrf_exempt
def verify(request, uid):
    print(uid)
    uid = str(uid)
    user = Users.objects.filter(uid=uid).first()
    if user:
        #print("User exists")
        if user.isVerified:
            return JsonResponse('Your account is already verified', safe = False)
        user.isVerified = True
        user.save()
        return JsonResponse('Your account has been verified', safe= False)
    return JsonResponse('No user found with this email', safe = False)



@api_view(['POST'])
@csrf_exempt
def login(request):
    #return JsonResponse("Reacher Here Successfully!!" , safe=False)
    if request.method == 'POST':
        #print("at least reached destination")
        users_data=JSONParser().parse(request)
        username = users_data['username']
        password = users_data['password']
        #print("username is ", username, "password is ", password)
        
        user = Users.objects.filter(username=username).first()

        if user is None:
            raise AuthenticationFailed('User not found')
        #elif user.isVerified==False:
            #raise AuthenticationFailed('Please verifiy your account first')
        elif not check_password(password, user.password):
            raise AuthenticationFailed('Incorrect Password')
    
        payload = {
            'username' : username,
            'exp' : datetime.datetime.utcnow()+datetime.timedelta(minutes=60),
            'iat' : datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256').decode('utf-8')

        response = Response()

        response.set_cookie(key='jwt', value=token, httponly=True, secure=False, samesite=None)
        response.data = {
            'jwt': token
        }
        return response
    
    return Response({
        'messsage' : 'Serialization Error'
    })


@api_view(['GET'])
@csrf_exempt
def userView(request):
    if request.method == 'GET':
        token = request.COOKIES.get('jwt')
        print(token)
        if not token:
            raise AuthenticationFailed('Unauthenticated!')

        try:
            payload = jwt.decode(token, 'secret', algorithm=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        print("HIH " + payload['username'])
        user = Users.objects.filter(username=payload['username']).first()
        serializer = UsersSerializer(user)
        return Response(serializer.data)

@api_view(['POST'])
@csrf_exempt
def logout(request):
    response = Response()
    response.delete_cookie('jwt')
    response.data = {
        'message': 'success'
    }
    return response

@api_view(['POST'])
@csrf_exempt
def api_call(request):
    if request.method == 'POST':
        # print(request.data)
        # return Response('asdasd')
        token = request.data['jwt']
        print(token)
        if not token:
            raise AuthenticationFailed('Unauthenticated!')

        try:
            payload = jwt.decode(token, 'secret', algorithm=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        #print(payload['username'])
        user = Users.objects.filter(username=payload['username']).first()
        username = user.username
        print("API_CALL")
        print(username)
        #username_as_bytes = str.encode(username)

        return Response(username)
        return Response(username_as_bytes)