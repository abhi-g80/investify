import pytest
from investify.investing import Investing


@pytest.fixture
def get_instrument():
    end_point = "/indices/us-spx-500"

    return Investing(end_point)


def test_contract_name(get_instrument):
    assert get_instrument.name == "us-spx-500"


def test_fetch_page(get_instrument):
    get_instrument.fetch()

    assert get_instrument.ok is True


def test_page(get_instrument):
    get_instrument.fetch()

    assert len(get_instrument.page) > 0
