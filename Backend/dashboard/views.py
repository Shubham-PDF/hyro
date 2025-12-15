from django.shortcuts import render
from django.db.models import Count, Max
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from accounts.permissions import IsRecruiter, IsApplicant
from jobs.models import Job
from applications.models import Application


# Create your views here.


# for the recruiter to see summary of their posted jobs
class RecruiterSummaryView(APIView):
    permission_classes = [IsAuthenticated, IsRecruiter]

    def get(self, request):

        # Get all jobs posted by this recruiter
        jobs = Job.objects.filter(created_by=request.user)

        # Annotate with applicant count + top score
        jobs_with_stats = jobs.annotate(
            applicants_count=Count('application'),
            top_score=Max('application__match_score')
        )

        # Prepare response
        job_list = [
            {
                "job_id": job.job_id,
                "title": job.title,
                "applicant_count": job.applicants_count,
                "top_match_score": job.top_score or 0
            }
            for job in jobs_with_stats
        ]

        total_applicants = sum(job["applicant_count"] for job in job_list)

        return Response({
            "total_jobs": jobs.count(),
            "total_applicants": total_applicants,
            "jobs": job_list
        })


# for. the applicant to see their application history

class ApplicantApplicationsView(APIView):
    permission_classes = [IsAuthenticated, IsApplicant]

    def get(self, request):

        # Get all applications of this user
        apps = Application.objects.filter(user=request.user).select_related("job")

        history = [
            {
                "job_id": app.job.job_id,
                "title": app.job.title,
                "applied_at": app.applied_at,
                "resume_url": app.resume_file,
                "company_name": app.job.company_name,
                "location": app.job.location,

            }
            for app in apps
        ]

        return Response(history)
