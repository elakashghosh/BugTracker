from html5lib import serialize
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from UsersApp.api.serializers import RegistrationSerializer, CustomUserSerializer
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from UsersApp import models
from rest_framework import generics
from UsersApp.models import CustomUser

class CustomAuthTokenAV(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'is_admin': user.is_staff,
        })

class Registration_view(APIView):
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data['message'] = "registration successfull"
            data['email'] = account.email
            data['token'] = Token.objects.get(user=account).key
        else:
            data = serializer.errors
        return Response(data)

class Logout_view(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)

class Is_activeList_view(generics.ListAPIView):
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get_queryset(self):
        return CustomUser.objects.filter(is_active = False)

class UpdateAccountStatus_view(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]

    def put(self, request, email, activate):
        if activate == 0:
            activate = False
        elif activate == 1:
            activate == True
        else:
            return Response({'message': 'Invalid parameter'}, status=status.HTTP_400_BAD_REQUEST)
        CustomUser.objects.filter(email=email).update(is_active=activate)
        return Response({'message': 'Updated'}, status=status.HTTP_200_OK)

class UserDetails(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get(self, request, pk):
        try:
            userDet = CustomUser.objects.get(pk=pk)
        except:
            return Response({}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = CustomUserSerializer(userDet)
        return Response(serializer.data, status=status.HTTP_200_OK)
