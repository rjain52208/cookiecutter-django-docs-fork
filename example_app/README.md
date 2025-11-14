# example_app

Minimal demo app for the Cookiecutter-Django production scaffold.

## What this app does

- Exposes a simple JSON **health-check endpoint** at `/health/`.
- Can be included from the main `urls.py` using:

```python
from django.urls import include, path

urlpatterns = [
    # ...
    path("", include("example_app.urls")),
]
```

- Returns service name and a UTC timestamp to verify the app is running.

## Why it exists

This app simulates a small feature module in a real-world Django project:

- separate `views.py` and `urls.py`
- clear responsibility (liveness/health probe)
- easy to extend with more endpoints later
