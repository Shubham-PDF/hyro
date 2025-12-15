from django.urls import path
from .views import (JobCreateView, JobUpdateView, JobActivateView, JobDeactivateView, JobListView, RecruiterJobsView, JobDetailView , JobDeleteView)

urlpatterns = [
    path('', JobListView.as_view()),
    path('create/', JobCreateView.as_view()),
    path('me/', RecruiterJobsView.as_view()),
    path('<uuid:job_id>/', JobDetailView.as_view()),
    path('<uuid:job_id>/edit/', JobUpdateView.as_view()),
    path('<uuid:job_id>/activate/', JobActivateView.as_view()),
    path('<uuid:job_id>/deactivate/', JobDeactivateView.as_view()),
    path("delete/<uuid:job_id>/", JobDeleteView.as_view()),
]