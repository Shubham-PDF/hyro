from django.urls import path
from .views import JobKeywordAIView

urlpatterns = [
    path("job-keywords/", JobKeywordAIView.as_view(), name="job-keywords"),
]
