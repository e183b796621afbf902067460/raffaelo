import pytest

from raffaelo.contracts.erc20.contract import ERC20TokenContract


@pytest.fixture(scope="module")
def allowance(contract: ERC20TokenContract, mock_address: str) -> int:  # noqa: D103
    yield contract.allowance(owner=mock_address, spender=mock_address)


def test__allowance__must_be_int(allowance: int):  # noqa: D103
    assert isinstance(allowance, int)
