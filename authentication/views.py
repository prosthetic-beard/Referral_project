from django.shortcuts import render
from account.models import Referral, UserProfile
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, get_user_model
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_api_payload import success_response, error_response
from authentication.serializers import ForgotPasswordSerializer, ResetPasswordSerializer, UserLoginSerializer, UserSerializer, UserSignUpSerializer, VerifyUserSerializer
from rest_framework.views import APIView
from authentication.models import User
import uuid



# Create your views here.

class Signup(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserSignUpSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            email = serializer.data['email']
            password = serializer.data['password']

            try:
                user = get_user_model().objects.get(email=email)
                if user:
                    payload = error_response(
                        status=False,
                        message= ["Email already exist."]
                    )
                    return Response(data=payload, status=status.HTTP_400_BAD_REQUEST)

            except get_user_model().DoesNotExist:
                user = get_user_model().objects.create_user(email=email, password=password)
                UserProfile.objects.create(user=user, account_balance=0)
                print(user.activation_token)
                # sendemail

            payload = success_response(
                status=True,
                message= ['Sign-up Successful. Kindly activate your email by clicking on the link sent to your email address'],
                data= serializer.data
            )
            return Response(data=payload, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class Login(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserLoginSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            email = serializer.data['email']
            password = serializer.data['password']
            user = authenticate(username=email, password=password)
            # user_login = User.objects.get(email=email)

            if user:
                if user.is_active:
                    token, created = Token.objects.get_or_create(user=user)
                    payload = success_response(
                        status=True,
                        message= ['Login Successful.'],
                        data= {'id': user.id, 'username': user.username, 'token': token.key, 'token': token.key, 'subscription': user.is_subscribed}
                    )
                    return Response(data=payload, status=status.HTTP_200_OK)
                else:
                    # sendemail
                    payload = error_response(
                        status=False,
                        message=['Your account is not active, An activation link has been sent to you email.']
                    )
                    return Response(data=payload, status=status.HTTP_401_UNAUTHORIZED)
            else:
                payload = error_response(
                        status=False,
                        message=['Invalid Username or password']
                )
                return Response(data=payload, status=status.HTTP_401_UNAUTHORIZED)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class Logout(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        """
        Remove all auth tokens owned by request.user.
        """
        tokens = Token.objects.filter(user=request.user)
        for token in tokens:
            token.delete()
        payload = success_response(
            status=True,
            message= ['Logout Successful.'],
            data= {}
        )
        return Response(data=payload, status=status.HTTP_200_OK)
    
class UserMe(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

    def get(self, request, format=None):
        serializer = self.serializer_class(request.user)
        payload = success_response(
            status=True,
            message=['User retrieved'],
            data= serializer.data
            )
        return Response(data=payload)
    
class ForgotPasswordView(generics.GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = ForgotPasswordSerializer

    

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)


        email = serializer.validated_data['email']

        try:
            user = User.objects.get(email=email)
            data = {
                'email': user.email,
            }
            # sendemail
            payload = success_response(
                status=True,
                message=["Successful, Kindly check your email for password reset link"],
                data=data
            )
            return Response(data=payload, status=status.HTTP_202_ACCEPTED)
        except User.DoesNotExist:
            payload = error_response(
                    status=False,
                    message=["Invalid email address"]
                )
            return Response(data=payload, status=status.HTTP_403_FORBIDDEN)
        

class ResetPasswordView(generics.GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = ResetPasswordSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)


        email = serializer.validated_data['email']
        password = serializer.validated_data['password']

        try:
            user = User.objects.get(email=email)
            user.password = password
            user.set_password(password)
            user.save()

            payload = success_response(
                status=True,
                message=["Successful, Your Password has been changed"],
            )
            return Response(data=payload, status=status.HTTP_202_ACCEPTED)

        except User.DoesNotExist:
            payload = error_response(
                    status=False,
                    message= ["Invalid user account"]
                )
            return Response(data=payload, status=status.HTTP_403_FORBIDDEN)
        
class VerifyUserView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = VerifyUserSerializer


    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        activation_token = serializer.validated_data['activation_token']
        referral_code = serializer.validated_data['referral_code']

        try:
            user = User.objects.get(activation_token=activation_token)
            try:
                referral = User.objects.get(referral_code=referral_code)
            except User.DoesNotExist:
                payload = success_response(
                    status=True,
                    message=["Referral code error, please try again"],
                )
                return Response(data=payload, status=status.HTTP_202_ACCEPTED)
            if user.is_active == True:
                payload = success_response(
                    status=True,
                    message=["Account is already active, please proceed to login"],
                )
                return Response(data=payload, status=status.HTTP_202_ACCEPTED)
            else:
                user.is_active = True
                referral_profile = UserProfile.objects.get(user=referral)
                referral_profile.account_balance += 100
                referral_profile.save()
                # user.activation_token = str(uuid.uuid5(uuid.uuid4(), user.email)).split("-")[0]
                user.activation_token = uuid.uuid4()
                user.save()
                Referral.objects.create(referral=referral_profile, referred_user=user)
                payload = success_response(
                    status=True,
                    message=["Activation successful"],
                )
                return Response(data=payload, status=status.HTTP_202_ACCEPTED)
        except User.DoesNotExist:
            payload = error_response(
                    status=False,
                    message= ["Invalid activation link"]
                )
            return Response(data=payload, status=status.HTTP_403_FORBIDDEN)