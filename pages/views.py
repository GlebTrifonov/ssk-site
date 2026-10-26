from django.shortcuts import render

from projects.models import Project
from services.models import Service


def home(request):
    services = Service.objects.filter(is_active=True)
    projects = (
        Project.objects.select_related("service")
        .prefetch_related("images")
        .filter(is_active=True)
    )
    context = {"services": services, "projects": projects}
    return render(request, "pages/home.html", context)
