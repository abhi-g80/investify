import os

import pytest
from investify.sendtext import SendText


@pytest.fixture
def send_text():
    return SendText("+123456789", "+3123456789")


def test_twilio_environment_variables():
    assert "TWILIO_ACCOUNT_SID" in os.environ
    assert "TWILIO_AUTH_TOKEN" in os.environ


def test_send_number(send_text):
    assert send_text.from_wsp_number == "whatsapp:+123456789"


def test_to_number(send_text):
    assert send_text.to_wsp_number == "whatsapp:+3123456789"
