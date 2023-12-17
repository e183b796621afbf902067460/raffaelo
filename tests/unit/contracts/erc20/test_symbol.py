import pytest

from raffaelo.contracts.erc20.contract import ERC20TokenContract


@pytest.fixture(scope="module")
def symbol(contract: ERC20TokenContract) -> str:  # noqa: D103
    yield contract.symbol()


def test__symbol__must_be_str(symbol: str):  # noqa: D103
    assert isinstance(symbol, str)


def test__symbol__must_be_equal_to_usdc(symbol: str):  # noqa: D103
    assert symbol == "USDC"
