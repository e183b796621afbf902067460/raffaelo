import pytest

from raffaelo.contracts.erc20.contract import ERC20TokenContract


@pytest.fixture(scope="module")
def decimals(contract: ERC20TokenContract) -> int:  # noqa: D103
    yield contract.decimals()


@pytest.mark.unit
def test__decimals__must_be_int(decimals: int):  # noqa: D103
    assert isinstance(decimals, int)


@pytest.mark.unit
def test__decimals__must_be_positive(decimals: int):  # noqa: D103
    assert decimals >= 0
