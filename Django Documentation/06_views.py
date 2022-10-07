# Edit web/views.py
import json

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse


def index(request):
    context = {"is_index": True}
    return render(request, "web/index.html", context)


def about(request):
    context = {"is_about": True}
    return render(request, "web/about.html", context)
