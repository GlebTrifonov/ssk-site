import pytest
import requests
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


@pytest.mark.django_db
def test_lead_create_sends_telegram_message(client, mocker, lead_data):
    mock_send = mocker.patch("leads.views.send_telegram_message")
    response = client.post(LEAD_CREATE_URL, data=lead_data)
    mock_send.assert_called_once()
    assert response.status_code == 302
    assert lead_data["name"] in mock_send.call_args.args[0]


@pytest.mark.django_db
def test_lead_create_survives_telegram_error(client, mocker, settings, lead_data):
    settings.TELEGRAM_BOT_TOKEN = "test_token"
    settings.TELEGRAM_CHAT_ID = "123"
    mock_post = mocker.patch("leads.telegram.requests.post")
    mock_post.side_effect = requests.exceptions.ConnectionError()
    response = client.post(LEAD_CREATE_URL, data=lead_data)
    assert response.status_code == 302
    assert Lead.objects.count() == 1
