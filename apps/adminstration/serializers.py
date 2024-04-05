from rest_framework import serializers

from apps.my_auth.models import Account, VerifyCode


class AdminLoginSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=20)
    password = serializers.CharField(max_length=45)

    class Meta:
        fields = ['phone', 'password']


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = [
            'id',
            'phone',
            'password',
            'first_name',
            'last_name',
            'middle_name',
            'birth_date',
            'avatar',
            'created_at',
            'updated_at',
            'user_status',
            'user_type',
            'is_superuser',
            'is_active',
            'is_staff',
        ]


class VerifyCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VerifyCode
        fields = [
            'id',
            'phone',
            'code',
            'created_at'
        ]
