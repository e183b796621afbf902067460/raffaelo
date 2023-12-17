import pytest

from raffaelo.contracts.erc20.contract import ERC20TokenContract


@pytest.fixture(scope="module")
def balance_of(contract: ERC20TokenContract, mock_address: str) -> int:  # noqa: D103
    yield contract.balanceOf(address=mock_address)


@pytest.mark.unit
def test__balance_of__must_be_int(balance_of: int):  # noqa: D103
    assert isinstance(balance_of, int)


@pytest.mark.unit
def test__balance_of__must_be_positive(balance_of: int):  # noqa: D103
    assert balance_of >= 0
