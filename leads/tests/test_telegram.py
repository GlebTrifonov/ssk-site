import requests

from leads.telegram import send_telegram_message


def test_send_telegram_message_posts_text(settings, mocker):
    settings.TELEGRAM_BOT_TOKEN = "test_token"
    settings.TELEGRAM_CHAT_ID = "123"
    mock_post = mocker.patch("leads.telegram.requests.post")
    send_telegram_message("Hello")
    mock_post.assert_called_once()
    assert mock_post.call_args.kwargs["json"]["text"] == "Hello"


def test_send_telegram_message_skips_without_token(mocker):
    mock_post = mocker.patch("leads.telegram.requests.post")
    send_telegram_message("Hello")
    mock_post.assert_not_called()


def test_send_telegram_message_sends_chat_id_and_timeout(settings, mocker):
    settings.TELEGRAM_BOT_TOKEN = "test_token"
    settings.TELEGRAM_CHAT_ID = "123"
    mock_post = mocker.patch("leads.telegram.requests.post")
    send_telegram_message("Hello")
    assert mock_post.call_args.kwargs["json"]["chat_id"] == "123"
    assert mock_post.call_args.kwargs["timeout"] == 5


def test_send_telegram_message_survives_network_error(settings, mocker):
    settings.TELEGRAM_BOT_TOKEN = "test_token"
    settings.TELEGRAM_CHAT_ID = "123"
    mock_post = mocker.patch("leads.telegram.requests.post")
    mock_post.side_effect = requests.exceptions.ConnectionError()
    send_telegram_message("Hello")
    mock_post.assert_called_once()
