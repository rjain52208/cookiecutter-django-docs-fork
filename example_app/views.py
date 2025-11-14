from datetime import datetime

from django.http import JsonResponse


def health_check(request):
    """
    Simple JSON health-check endpoint.

    This can be wired into Django's URL config to verify that
    the app, database connection, and environment are working.
    """
    return JsonResponse(
        {
            "status": "ok",
            "service": "cookiecutter-django-production-scaffold",
            "timestamp": datetime.utcnow().isoformat() + "Z",
        }
    )
