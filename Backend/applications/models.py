from django.db import models
from jobs.models import Job
from django.conf import settings
# Create your models here.

class Application(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    
    resume_file = models.URLField(blank=True, null=True)  # Cloudinary URL for resume
    extracted_text = models.TextField(blank=True)
    match_score = models.FloatField(default=0)

    applied_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'job')  # prevent multople apply to single job by single user 

    def __str__(self):
        return f"{self.user.username} → {self.job.title}"
