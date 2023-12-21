from rest_framework.decorators import api_view
from .serializers import RegistrationSerializer 
from rest_framework.response import Response
from user_app import models 
from rest_framework import status
from rest_framework.authtoken.models import Token
@api_view(['POST'])
def logout_view(request):
    if request.method=='POST':
        request.user.auth_token.delete()
        return Response(status=HTTP_200_OK)

@api_view(['POST'])
def Registration_view(request):
    if request.method=='POST':
        serializer=RegistrationSerializer(data=request.data)
        data={}
        if serializer.is_valid():
            account=serializer.save()
            data['Response']='Registration Successful'
            data['username']=account.username
            data['email']=account.email

            token = Token.objects.get(user=account).key
            data['token']=token
        else:
            serializer.errors
        return Response(data)