from django.db import models
from django.conf import settings
from django.contrib.postgres.fields import ArrayField
import uuid

# Create your models here.

class Job(models.Model):
    job_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='jobs'
    )

    title = models.CharField(max_length=255)
    description = models.TextField()
    company_name = models.CharField(max_length=255)
    requirements = models.TextField(blank=True)



    keywords = ArrayField(
        models.CharField(max_length=50),
        blank=True,
        default=list
    )

    location = models.CharField(max_length=255)
    experience_required = models.CharField(max_length=255)
    
    salary_min = models.IntegerField(null=True, blank=True)
    salary_max = models.IntegerField(null=True, blank=True)

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
