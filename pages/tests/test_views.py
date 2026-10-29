import pytest
from django.urls import reverse

from projects.models import Project, Review
from services.models import Service


@pytest.mark.django_db
def test_home_shows_only_active_services(client):
    active = Service.objects.create(title="Active")
    hidden = Service.objects.create(title="Hidden", is_active=False)
    response = client.get(reverse("home"))
    assert response.status_code == 200
    assert active in response.context["services"]
    assert hidden not in response.context["services"]


@pytest.mark.django_db
def test_home_shows_only_active_reviews(client):
    active = Review.objects.create(author="Active", text="test_active")
    hidden = Review.objects.create(author="Hidden", text="text_hidden", is_active=False)
    response = client.get(reverse("home"))
    assert response.status_code == 200
    assert active in response.context["reviews"]
    assert hidden not in response.context["reviews"]


@pytest.mark.django_db
def test_home_shows_only_active_projects(client):
    service = Service.objects.create(title="Roof")
    active = Project.objects.create(title="Active", service=service)
    hidden = Project.objects.create(title="Hidden", service=service, is_active=False)
    response = client.get(reverse("home"))
    assert response.status_code == 200
    assert active in response.context["projects"]
    assert hidden not in response.context["projects"]
