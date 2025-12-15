from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    ROLES = (
        ('recruiter', 'Recruiter'),
        ('applicant', 'Applicant'),
    )

    role = models.CharField(max_length=10 , choices= ROLES)
    full_name = models.CharField(max_length=150)
    phone = models.CharField(max_length=20, blank=True, null=True)
    about = models.TextField(blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)
    github_url = models.URLField(blank=True, null=True)
    portfolio_url = models.URLField(blank=True, null=True)
    skills = models.JSONField(default=list, blank=True, null=True)

    def __str__(self):
        return self.username