from django.urls import path
from django.views.generic import TemplateView

from pages.views import home

urlpatterns = [
    path("", home, name="home"),
    path(
        "privacy/",
        TemplateView.as_view(template_name="pages/privacy.html"),
        name="privacy",
    ),
]
