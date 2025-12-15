from rest_framework import serializers
from .models import Application
from django.contrib.auth import get_user_model
class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = '__all__'
        read_only_fields = ['user' , 'job', 'match_score', 'extracted_text', 'applied_at']

class ApplicationDetailSerializer(serializers.ModelSerializer):
    """Serializer that includes full job details for applicant's view"""
    job_details = serializers.SerializerMethodField()
    
    class Meta:
        model = Application
        fields = ['id', 'job', 'job_details', 'resume_file', 'match_score', 'applied_at']
        read_only_fields = ['id', 'job', 'match_score', 'applied_at']
    
    def get_job_details(self, obj):
        """Return detailed job information"""
        return {
            'job_id': str(obj.job.job_id),
            'title': obj.job.title,
            'company_name': obj.job.company_name,
            'location': obj.job.location,
            'description': obj.job.description,
            'experience_required': obj.job.experience_required,
            'salary_min': obj.job.salary_min,
            'salary_max': obj.job.salary_max,
            'is_active': obj.job.is_active,
            'created_at': obj.job.created_at,
        }

User = get_user_model()

class CandidateSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'full_name',
            'skills',
        ]

class RecruiterApplicationSerializer(serializers.ModelSerializer):
    candidate = CandidateSummarySerializer(source='user', read_only=True)

    class Meta:
        model = Application
        fields = [
            'id',
            'candidate',
            'match_score',
            'resume_file',
            'applied_at',
        ]
