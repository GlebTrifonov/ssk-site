from django.urls import reverse_lazy

LEAD_CREATE_URL = reverse_lazy("lead_create")


def test_lead_create_page_opens(client):
    response = client.get(LEAD_CREATE_URL)
    assert response.status_code == 200
    assert "form" in response.context
