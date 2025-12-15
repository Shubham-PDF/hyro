from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()
class SignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True)

    class Meta:
        model = User
        fields = ["username", "email", "password", "role", "full_name", "phone"]
    
    def validate_username(self, value):
        """Check if username already exists"""
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("Username already exists.")
        return value
    
    def validate_email(self, value):
        """Check if email already exists"""
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already exists.")
        return value
    
    def create(self, validated_data):
        print(serializers.ErrorDetail)
        user = User(
            username = validated_data['username'],
            email = validated_data['email'],
            role = validated_data['role'],
            full_name = validated_data.get('full_name', ''),
            phone = validated_data.get('phone', '')
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class ProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "full_name",
            "phone",
            "about",
            "linkedin_url",
            "github_url",
            "portfolio_url",
            "skills",
        ]

class CandidateDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'full_name',
            'email',
            'phone',
            'about',
            'skills',
            'linkedin_url',
            'github_url',
            'portfolio_url',
        ]
