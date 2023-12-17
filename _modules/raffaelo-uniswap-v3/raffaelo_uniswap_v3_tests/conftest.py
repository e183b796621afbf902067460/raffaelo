import pytest
from raffaelo_uniswap_v3.pool.contract import UniSwapV3PoolContract

from raffaelo.providers.http.provider import HTTPProvider


@pytest.fixture(scope="package")
def provider() -> HTTPProvider:  # noqa: D103
    return HTTPProvider(uri="https://rpc.ankr.com/eth")


@pytest.fixture(scope="package")
def pool(provider: HTTPProvider) -> UniSwapV3PoolContract:  # noqa: D103
    return UniSwapV3PoolContract(address="0x88e6A0c2dDD26FEEb64F039a2c41296FcB3f5640", provider=provider)
