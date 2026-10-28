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

@pytest.mark.django_db
def test_lead_create_invalid_phone_not_saved(client, lead_data):
    lead_data["phone"] = "+4455298308649"
    response = client.post(LEAD_CREATE_URL, data=lead_data)
    assert response.status_code == 200
    assert "phone" in response.context["form"].errors
    assert Lead.objects.count() == 0