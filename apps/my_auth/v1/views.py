from random import randint
from rest_framework import generics, status, authentication, permissions
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import LoginSerializer, RegisterSerializer, LoginVerifySerializer
from ..models import Account, VerifyCode
from ...tools.helpers import send_sms


class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        phone = Account.objects.filter(phone=request.data['phone']).first()
        if not phone:
            return Response({"message": "This number is not registered"}, status=407)
        verify = VerifyCode.objects.filter(phone=phone).first()
        if verify:
            verify.delete()
        verification_code = str(randint(10000, 100000))
        send_sms(request.data['phone'], verification_code)
        VerifyCode.objects.create(phone=request.data['phone'], code=verification_code)
        return Response({"success": True, 'message': "A confirmation code was sent to the phone number!!!"},
                        status=status.HTTP_200_OK)


class LoginVerifyAPIView(generics.GenericAPIView):
    serializer_class = LoginVerifySerializer

    def post(self, request, *args, **kwargs):
        phone = request.data['phone']
        code = request.data['code']
        verify = VerifyCode.objects.filter(phone=phone, code=code).first()
        if not verify:
            return Response({"message": "The confirmation code is  incorrect!"}, status=404)
        verify.delete()
        user = Account.objects.filter(phone=phone).first()
        user.is_active = True
        user.save()
        try:
            token = Token.objects.get(user=user)
        except:
            token = Token.objects.create(user=user)
        return Response({
            "success": True,
            "message": "User successfully verified",
            "token": str(token),
            "user_id": user.id
        }, status=200)


class RegisterAPIView(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = RegisterSerializer(data=request.data)
        user = None
        if serializer.is_valid(raise_exception=True):
            user = Account.objects.filter(phone=serializer.validated_data['phone']).first()
        if user:
            return Response({"message": "This number is already registered"}, status=400)
        verify = VerifyCode.objects.filter(phone=request.data['phone']).first()
        if verify:
            verify.delete()
        verification_code = str(randint(10000, 100000))
        send_sms(request.data['phone'], verification_code)
        VerifyCode.objects.create(phone=request.data['phone'], code=verification_code)
        serializer.save(is_active=False, password='12345678')
        return Response({"success": True, 'message': "A confirmation code was sent to the phone number!!!"},
                        status=status.HTTP_200_OK)


class RegisterVerifyView(generics.GenericAPIView):
    serializer_class = LoginVerifySerializer

    def post(self, request, *args, **kwargs):
        phone = request.data['phone']
        code = request.data['code']
        verify = VerifyCode.objects.filter(phone=phone, code=code).first()
        if not verify:
            return Response({"message": "The confirmation code is  incorrect!"}, status=404)
        verify.delete()
        user = Account.objects.filter(phone=phone).first()
        user.is_active = True
        user.save()
        try:
            token = Token.objects.get(user=user)
        except:
            token = Token.objects.create(user=user)
        return Response({
            "success": True,
            "message": "User successfully verified",
            "token": str(token),
            "user_id": user.id
        }, status=200)


class LogoutView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = self.request.user
        token = Token.objects.get(user=user)
        token.delete()
        return Response({"success": True, 'message': 'logged out'}, status=200)


class DeleteAccountView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = Account.objects.filter(id=self.request.user.id).first()
        user.is_active = False
        user.save()
        return Response({"success": True, 'message': 'Account has been deleted'}, status=200)
