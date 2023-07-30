from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
import re





User = get_user_model()
User.__init__.unique = True

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'email', 'company_name', 'is_subscribed')


class UserSignUpSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=300, required=True)
    password = serializers.CharField(required=True)
    confirm_password = serializers.CharField(required=True)

    def validate(self, attrs):
        password = attrs.get('password')
        confirm_password = attrs.get('confirm_password')
        if not any(char.isdigit() for char in password):
            raise ValidationError("Password must contain at least 1 number.")
        if not any(char.isalpha() for char in password):
            raise ValidationError("Password must contain at least 1 alphabet character.")
        if not any(not char.isalnum() for char in password):
            raise ValidationError("Password must contain at least 1 symbol.")
        if password != confirm_password:
            raise ValidationError("Password does not match.")
        if not re.fullmatch(r"[A-Za-z0-9@#$%^&+=-]{8,}", password):
            raise ValidationError("Password must be more than 8 characters")
        return super().validate(attrs)

class UserLoginSerializer(serializers.Serializer):
    """
    A user serializer for logging in the user
    """
    email = serializers.CharField(max_length=300, required=True)
    password = serializers.CharField(required=True)

    extra_kwargs = {
        "password": {
            "write_only": True
        }
    }


class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()

class ResetPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
    confirm_password = serializers.CharField()

    def validate(self, attrs):
        password = attrs.get('password')
        confirm_password = attrs.get('confirm_password')
        if not any(char.isdigit() for char in password):
            raise ValidationError("Password must contain at least 1 number.")
        if not any(char.isalpha() for char in password):
            raise ValidationError("Password must contain at least 1 alphabet character.")
        if not any(not char.isalnum() for char in password):
            raise ValidationError("Password must contain at least 1 symbol.")
        if password != confirm_password:
            raise ValidationError("Password does not match.")
        if not re.fullmatch(r"[A-Za-z0-9@#$%^&+=-]{8,}", password):
            raise ValidationError("Password must be more than 8 characters")
        return super().validate(attrs)
    
class VerifyUserSerializer(serializers.Serializer):
    activation_token = serializers.CharField()
    referral_code = serializers.CharField()
