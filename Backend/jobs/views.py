from django.shortcuts import render
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView , UpdateAPIView , ListAPIView , RetrieveAPIView , DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from accounts.permissions import IsRecruiter
from .serializers import JobSerializer
from .models import Job
from rest_framework.response import Response
from rest_framework import status
from core.pagination import JobPagination


# Create your views here.

class JobCreateView(CreateAPIView):
    serializer_class = JobSerializer
    permission_classes = [IsAuthenticated, IsRecruiter]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class JobUpdateView(UpdateAPIView):
    serializer_class = JobSerializer
    permission_classes = [IsAuthenticated, IsRecruiter]
    lookup_field = "job_id"

    def get_queryset(self):
        # ensures recruiter only edits their own jobs
        return Job.objects.filter(created_by=self.request.user)
    

class JobActivateView(APIView):
    permission_classes = [IsAuthenticated, IsRecruiter]

    def patch(self, request, job_id):
        try:
            job = Job.objects.get(job_id=job_id, created_by=request.user)
            job.is_active = True
            job.save()
            return Response({"message": "Job activated"}, status=status.HTTP_200_OK)
        except Job.DoesNotExist:
            return Response({"error": "Job not found"}, status=status.HTTP_404_NOT_FOUND)

class JobDeactivateView(APIView):
    permission_classes = [IsAuthenticated , IsRecruiter]

    def patch(self , request , job_id):
        try:
            job = Job.objects.get(job_id = job_id , created_by = request.user)
            job.is_active = False
            job.save()
            return Response({"message" : "Job Deactivated"} , status= status.HTTP_200_OK)
        except Job.DoesNotExist:
            return Response({"error": "Job not Found"} , status= status.HTTP_404_NOT_FOUND)
 
class JobDeleteView(DestroyAPIView):
    serializer_class = JobSerializer
    permission_classes = [IsAuthenticated, IsRecruiter]
    lookup_field = "job_id"

    def get_queryset(self):
        qs = Job.objects.filter(created_by=self.request.user)
        print("DELETE USER:", self.request.user)
        print("JOBS OWNED:", qs.values_list("job_id", flat=True))
        return qs      

class JobListView(ListAPIView):
    serializer_class = JobSerializer
    pagination_class = JobPagination

    # def get_queryset(self):
    #     queryset = Job.objects.filter(is_active=True)

    #     search = self.request.query_params.get("search")
    #     if search:
    #         queryset = queryset.filter(
    #             Q(title__icontains=search) |
    #             Q(description__icontains=search) |
    #             Q(keywords__icontains=search)
    #         )
    #     return queryset.order_by('-created_at')
    def get_queryset(self):
        qs = Job.objects.filter(is_active=True)

        search = self.request.query_params.get("search")
        location = self.request.query_params.get("location")
        exp = self.request.query_params.get("exp")
        min_salary = self.request.query_params.get("min_salary")
        max_salary = self.request.query_params.get("max_salary")

        if search:
            qs = qs.filter(
                Q(title__icontains=search) |
                Q(description__icontains=search) |
                Q(keywords__icontains=search)
            )

        if location:
            qs = qs.filter(location__icontains=location)

        if exp:
            qs = qs.filter(experience_required__lte=exp)

        if min_salary:
            qs = qs.filter(salary_min__gte=min_salary)

        if max_salary:
            qs = qs.filter(salary_max__lte=max_salary)

        return qs.order_by("-created_at")



class RecruiterJobsView(ListAPIView):
    serializer_class = JobSerializer
    permission_classes = [IsAuthenticated, IsRecruiter]

    def get_queryset(self):
        return Job.objects.filter(created_by=self.request.user).order_by('-created_at')


class JobDetailView(RetrieveAPIView):
    serializer_class = JobSerializer
    queryset = Job.objects.all()
    lookup_field = "job_id"


    