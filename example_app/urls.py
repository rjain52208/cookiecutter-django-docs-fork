from django.urls import path

from .views import health_check

# Minimal URL configuration for the example_app.
# This can be included from the main project's urls.py.
urlpatterns = [
    path("health/", health_check, name="health-check"),
]
