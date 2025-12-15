from rest_framework import serializers
from .models import Job

class JobSerializer(serializers.ModelSerializer):

    applicant_count = serializers.SerializerMethodField()

    def get_applicant_count(self, obj):
        return obj.application_set.count()
    
    class Meta:
        model = Job
        fields = [
            'job_id',
            'title',
            'description',
            'keywords',
            'location',
            'experience_required',
            'salary_min',
            'salary_max',
            'is_active',
            'created_at',
            'applicant_count',
            'company_name',
            'requirements'
        ]
        read_only_fields = ['job_id', 'created_at', 'is_active']

    def validate_keywords(self, value):
        if not isinstance(value, list):
            raise serializers.ValidationError("Keywords must be a list.")
        if len(value) == 0:
            raise serializers.ValidationError("At least one keyword is required.")
        return value

    def validate(self, data):
        salary_min = data.get("salary_min")
        salary_max = data.get("salary_max")

        if salary_min and salary_max and salary_min > salary_max:
            raise serializers.ValidationError("Minimum salary cannot be greater than maximum salary.")
        
        return data

    def to_representation(self, instance):
        data = super().to_representation(instance)

        request = self.context.get("request")

        # Hide keywords unless recruiter is viewing
        if request and request.user.role != "recruiter":
            data.pop("keywords", None)

        return data