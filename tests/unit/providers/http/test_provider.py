import pytest

from raffaelo.providers.http.provider import HTTPProvider


@pytest.mark.unit
def test__provider__must_be_http_provider(provider: HTTPProvider):  # noqa: D103
    assert isinstance(provider, HTTPProvider)
