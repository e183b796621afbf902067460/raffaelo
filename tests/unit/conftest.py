import pytest

from raffaelo.providers.http.provider import HTTPProvider


@pytest.fixture(scope="package")
def provider() -> HTTPProvider:  # noqa: D103
    return HTTPProvider(uri="https://rpc.ankr.com/eth")
