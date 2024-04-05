from ..models import Account, VerifyCode
from rest_framework import serializers


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['phone']


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['phone', 'first_name', 'last_name', 'middle_name', 'avatar', 'birth_date', 'user_type', 'user_status']


class LoginVerifySerializer(serializers.ModelSerializer):
    class Meta:
        model = VerifyCode
        fields = ['phone', 'code', 'created_at']



