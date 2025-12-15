from django.urls import path
from .views import RecruiterSummaryView, ApplicantApplicationsView

urlpatterns = [
    path("recruiter/summary/", RecruiterSummaryView.as_view()),
    path("applicant/applications/", ApplicantApplicationsView.as_view()),
]
