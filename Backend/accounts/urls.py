from django.urls import path
from .views import SignupView, MeView , ProfileUpdateView, DeleteUserView , CandidateByUsernameView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('signup/', SignupView.as_view()),
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('me/', MeView.as_view()),
    path('me/update/', ProfileUpdateView.as_view()),
    path('me/delete/', DeleteUserView.as_view()),
    path('candidates/<str:username>/', CandidateByUsernameView.as_view()),
]
