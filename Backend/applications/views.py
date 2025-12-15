import logging
from django.db import transaction, IntegrityError
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from accounts.permissions import IsApplicant, IsRecruiter
from .models import Application
from .serializers import  RecruiterApplicationSerializer
from .services import extract_resume_text, compute_match_score
from jobs.models import Job
from django.conf import settings

from .supabase_client import supabase

logger = logging.getLogger(__name__)
from django.conf import settings
print("SUPABASE KEY STARTS WITH:", settings.SUPABASE_KEY[:10])


class ApplyJobView(APIView):
    permission_classes = [IsAuthenticated, IsApplicant]

    def post(self, request, job_id):

        # 1. Validate job
        try:
            job = Job.objects.get(job_id=job_id, is_active=True)
        except Job.DoesNotExist:
            return Response({"error": "Job not found or inactive"}, status=404)

        # 2. Validate resume
        resume = request.FILES.get("resume")
        if not resume:
            return Response({"error": "Resume file is required"}, status=400)

        # 3. Prevent duplicate applications
        if Application.objects.filter(user=request.user, job=job).exists():
            return Response({"error": "Already applied to this job"}, status=400)

        try:
            # Extract text
            resume.seek(0)
            resume_bytes = resume.read()
            extracted_text = extract_resume_text(resume_bytes)

            score = compute_match_score(extracted_text, job.keywords)

            # Supabase upload path
            file_path = f"{request.user.id}/{job.job_id}/{resume.name}"

            try:
                # Upload to Supabase
                upload_response = supabase.storage.from_(settings.SUPABASE_BUCKET).upload(
                    file_path,
                    resume_bytes,
                    {
                        "content-type": "application/pdf",
                        "x-upsert": "true"
                    }
                )
                logger.info(f"Upload response: {upload_response}")

                # Public URL
                public_url = supabase.storage.from_(settings.SUPABASE_BUCKET).get_public_url(file_path)
                logger.info(f"Generated public URL: {public_url}")
            except Exception as upload_error:
                logger.error(f"Supabase upload error details: {type(upload_error).__name__} - {str(upload_error)}")
                raise

            # Save Application
            with transaction.atomic():
                application = Application.objects.create(
                    user=request.user,
                    job=job,
                    resume_file=public_url,
                    extracted_text=extracted_text,
                    match_score=score
                )

            return Response({
                "message": "Application submitted successfully",
                "match_score": score,
                "resume_url": public_url,
                "application_id": application.id
            }, status=201)

        except Exception as e:
            logger.error(f"Supabase upload error: {str(e)}")
            return Response({"error": "Upload failed"}, status=500)


class JobApplicantsView(APIView):
    permission_classes = [IsAuthenticated, IsRecruiter]

    def get(self, request, job_id):
        job = Job.objects.get(job_id=job_id, created_by=request.user)

        applicants = (
            Application.objects
            .filter(job=job)
            .select_related('user')
            .order_by('-match_score')
        )

        serializer = RecruiterApplicationSerializer(applicants, many=True)

        return Response({
            'job_id': job_id,
            'total_applicants': applicants.count(),
            'applicants': serializer.data
        })

    
class MyApplicationsView(APIView):
    """View for applicants to see their own job applications"""
    permission_classes = [IsAuthenticated, IsApplicant]

    def get(self, request):
        """Get all applications submitted by the authenticated applicant"""
        applications = Application.objects.filter(user=request.user).order_by("-applied_at")
        
        if not applications.exists():
            return Response({
                "message": "No applications found",
                "applications": []
            }, status=status.HTTP_200_OK)
        
        from .serializers import ApplicationDetailSerializer
        serializer = ApplicationDetailSerializer(applications, many=True)
        
        return Response({
            "message": "Applications retrieved successfully",
            "total_applications": applications.count(),
            "applications": serializer.data
        }, status=status.HTTP_200_OK)

