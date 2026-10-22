from django.shortcuts import render

from services.models import Service


def home(request):
    services = Service.objects.filter(is_active=True)
    context = {
        "services": services
    }
    return render(request, "pages/home.html", context)
