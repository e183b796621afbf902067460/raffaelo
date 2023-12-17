import pytest
from raffaelo_quickswap_v3.pool.contract import QuickSwapV3AlgebraPoolContract

from raffaelo.providers.http.provider import HTTPProvider


@pytest.fixture(scope="package")
def provider() -> HTTPProvider:  # noqa: D103
    return HTTPProvider(uri="https://rpc.ankr.com/polygon")


@pytest.fixture(scope="package")
def pool(provider: HTTPProvider) -> QuickSwapV3AlgebraPoolContract:  # noqa: D103
    return QuickSwapV3AlgebraPoolContract(address="0xAE81FAc689A1b4b1e06e7ef4a2ab4CD8aC0A087D", provider=provider)
