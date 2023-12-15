from raffaelo.providers.http.provider import HTTPProvider


def test__provider__must_be_http_provider(provider: HTTPProvider):  # noqa: D103
    assert isinstance(provider, HTTPProvider)


def test__provider_protocol__must_be_str(provider: HTTPProvider):  # noqa: D103
    assert isinstance(provider._protocol, str)


def test__provider_protocol__must_be_equal_to_http(provider: HTTPProvider):  # noqa: D103
    assert provider._protocol == "http"


def test__provider_uri__must_be_str(provider: HTTPProvider):  # noqa: D103
    assert isinstance(provider._uri, str)


def test__provider_uri__must_be_equal_to_ankr(provider: HTTPProvider):  # noqa: D103
    assert provider._uri == "https://rpc.ankr.com/eth"
