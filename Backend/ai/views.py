from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.conf import settings

from google import genai
import re

class JobKeywordAIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        
        if request.user.role != "recruiter":
            return Response(
                {"detail": "Only recruiters can generate keywords"},
                status=status.HTTP_403_FORBIDDEN
            )

       
        description = request.data.get("description", "").strip()

        if not description:
            return Response(
                {"detail": "Description is required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        if len(description) > 2000:
            return Response(
                {"detail": "Description too long"},
                status=status.HTTP_400_BAD_REQUEST
            )

        
        client = genai.Client()
        prompt = f"""
            You are an expert technical recruiter.

            From the job description below, extract 5 to 6 concise, relevant technical skills or keywords which exactly matched with the given description.

            Rules:
            - Return ONLY a comma-separated list
            - No explanations
            - No numbering
            - No extra text
            - Keywords must be short (1 to 3 words)

            Job Description:
            \"\"\"
            {description}
            \"\"\"
            """

        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash", contents=prompt
            )
            raw_text = response.text
        except Exception:
            return Response(
                {"detail": "AI service unavailable"},
                status=status.HTTP_503_SERVICE_UNAVAILABLE
            )

        
        keywords = [
            re.sub(r"[^a-zA-Z0-9 +#.-]", "", k).strip().title()
            for k in raw_text.split(",")
        ]

        # Remove empty & duplicates
        keywords = list(dict.fromkeys(filter(None, keywords)))

        # Enforce limit
        keywords = keywords[:6]

        return Response({"keywords": keywords}, status=status.HTTP_200_OK)
