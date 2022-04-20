from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import Blog
from .forms import ContactForm


# Added blogs
def index(request):
    blogs = Blog.objects.filter(is_active=True)
    context = {
        "is_index": True,
        "blogs": blogs,
    }
    return render(request, "web/index.html", context)


def blogview(request, slug):
    instance = get_object_or_404(Blog, slug=slug)
    context = {
        "is_blog": True,
        "instance": instance,
    }
    return render(request, "web/blog.html", context)


def contact(request):
    form = ContactForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            response_data = {
                "status": "true",
                "title": "Successfully Submitted",
                "message": "Message successfully updated",
            }
        else:
            print(form.errors)
            response_data = {
                "status": "false",
                "title": "Form validation error",
            }
        return HttpResponse(
            json.dumps(response_data), content_type="application/javascript"
        )
    else:
        context = {
            "is_contact": True,
            "form": form,
        }
    return render(request, "web/contact.html", context)
