"""
When working with multiple and separate `views`, you may load different data objects into different views, 
but sometimes the use case requires you to have the same data available across the entire application. 
That’s exactly where custom context processors can be very useful. To create a custom context processor, 
add a new file inside your app folder.
"""

# web/context_processors.py
import datetime


def main_context(request):
    today = datetime.date.today()
    return {
        "domain": request.META["HTTP_HOST"],
    }


# Map to template Context Processors Engine
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                ...
                "web.context_processors.main_context",
            ],
        },
    },
]
