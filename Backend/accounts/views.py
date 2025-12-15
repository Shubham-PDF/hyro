from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin
from .serializers import SignupSerializer
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated , AllowAny as allowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ProfileUpdateSerializer
from rest_framework import status
from .serializers import CandidateDetailSerializer
from .models import CustomUser
from django.shortcuts import get_object_or_404
User = get_user_model()

class SignupView(CreateModelMixin, GenericAPIView):
    permission_classes = [allowAny]
    serializer_class = SignupSerializer
    queryset = User.objects.all()

    def post(self, request, *args, **kwargs):
        print(request.data)
        return self.create(request, *args, **kwargs)

class MeView(GenericAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request,):
        user = request.user
        return Response({
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "role": user.role,
            "full_name": user.full_name,
            "phone": user.phone,
            "linkedin_url": user.linkedin_url,
            "github_url": user.github_url,
            "about": user.about,
            "skills": user.skills,
            "portfolio_url": user.portfolio_url,

        })

class ProfileUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request):
        user = request.user
        serializer = ProfileUpdateSerializer(user, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Profile updated successfully"})
        
        return Response(serializer.errors, status=400)

class DeleteUserView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request):
        user = request.user
        user.delete()
        return Response({"message": "User deleted successfully"}, status=204)

class CandidateByUsernameView(GenericAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, username):
        candidate = get_object_or_404(
            CustomUser,
            username=username,
            role='applicant'
        )
        def build_user_profile_response(user):
            return {
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "role": user.role,
                "full_name": user.full_name,
                "phone": user.phone,
                "linkedin_url": user.linkedin_url,
                "github_url": user.github_url,
                "about": user.about,
                "skills": user.skills,
                "portfolio_url": user.portfolio_url,
            }
        return Response(
            build_user_profile_response(candidate)
        )