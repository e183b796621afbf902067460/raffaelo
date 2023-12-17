import pytest

from raffaelo.contracts.erc20.contract import ERC20TokenContract


@pytest.fixture(scope="module")
def total_supply(contract: ERC20TokenContract) -> int:  # noqa: D103
    yield contract.totalSupply()


@pytest.mark.unit
def test__total_supply__must_be_int(total_supply: int):  # noqa: D103
    assert isinstance(total_supply, int)


@pytest.mark.unit
def test__total_supply__must_be_positive(total_supply: int):  # noqa: D103
    assert total_supply >= 0
