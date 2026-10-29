import pytest


@pytest.fixture(autouse=True)
def disable_telegram(settings):
    settings.TELEGRAM_BOT_TOKEN = ""
