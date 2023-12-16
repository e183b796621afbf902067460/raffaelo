import pytest

from raffaelo.contracts.erc20.contract import ERC20TokenContract


@pytest.fixture(scope="module")
def name(contract: ERC20TokenContract) -> str:  # noqa: D103
    yield contract.name()


def test__name__must_be_str(name: str):  # noqa: D103
    assert isinstance(name, str)


def test__name__must_be_equal_to_usd_coin(name: str):  # noqa: D103
    assert name == "USD Coin"
