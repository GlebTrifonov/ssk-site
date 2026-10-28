import pytest
from django.urls import reverse, reverse_lazy

from leads.models import Lead

LEAD_CREATE_URL = reverse_lazy("lead_create")


def test_lead_create_page_opens(client):
    response = client.get(LEAD_CREATE_URL)
    assert response.status_code == 200
    assert "form" in response.context


@pytest.mark.django_db
def test_lead_create_saves_lead(client):
    response = client.post(
        LEAD_CREATE_URL, data={"name": "Alex", "phone": "+375298308649"}
    )
    assert response.status_code == 302
    assert response.url == reverse("home")
    assert Lead.objects.count() == 1
