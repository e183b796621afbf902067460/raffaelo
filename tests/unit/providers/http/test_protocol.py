import pytest

from raffaelo.providers.http.provider import HTTPProvider


@pytest.mark.unit
def test__protocol__must_be_str(provider: HTTPProvider):  # noqa: D103
    assert isinstance(provider._protocol, str)


@pytest.mark.unit
def test__protocol__must_be_equal_to_http(provider: HTTPProvider):  # noqa: D103
    assert provider._protocol == "http"
