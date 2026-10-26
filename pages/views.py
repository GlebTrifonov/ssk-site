from django.shortcuts import render

from projects.models import Project, Review
from services.models import Service


def home(request):
    services = Service.objects.filter(is_active=True)
    projects = (
        Project.objects.select_related("service")
        .prefetch_related("images")
        .filter(is_active=True)
    )
    reviews = Review.objects.filter(is_active=True)[:6]
    context = {"services": services, "projects": projects, "reviews": reviews}
    return render(request, "pages/home.html", context)
