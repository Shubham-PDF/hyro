from django.urls import path
from .views import ApplyJobView, JobApplicantsView, MyApplicationsView 

urlpatterns = [
    path('my-applications/', MyApplicationsView.as_view(), name='my-applications'),
    path('<uuid:job_id>/apply/', ApplyJobView.as_view(), name='apply-job'),
    path('<uuid:job_id>/applicants/', JobApplicantsView.as_view(), name='job-applicants'),

]
