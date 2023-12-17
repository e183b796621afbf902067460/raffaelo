import pytest

from raffaelo.contracts.erc20.contract import ERC20TokenContract
from raffaelo.providers.http.provider import HTTPProvider


@pytest.fixture(scope="module")
def contract(provider: HTTPProvider) -> ERC20TokenContract:  # noqa: D103
    yield ERC20TokenContract(address="0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48", provider=provider)


@pytest.fixture(scope="module")
def mock_address() -> str:  # noqa: D103
    yield "0x8BD4B2312f6C95B0D40E7407b26b124B25cbA375"
