from supabase import create_client
from django.conf import settings
import logging

logger = logging.getLogger(__name__)

# Verify credentials are loaded
if not settings.SUPABASE_URL or not settings.SUPABASE_KEY:
    logger.error("Supabase credentials not configured in settings")
    raise ValueError("SUPABASE_URL and SUPABASE_KEY must be set in environment")

supabase = create_client(
    settings.SUPABASE_URL,
    settings.SUPABASE_KEY
)
