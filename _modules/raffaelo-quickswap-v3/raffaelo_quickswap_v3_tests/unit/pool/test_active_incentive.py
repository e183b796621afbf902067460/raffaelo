import pytest
from raffaelo_quickswap_v3.pool.contract import QuickSwapV3AlgebraPoolContract
from web3 import Web3


@pytest.fixture(scope="module")
def active_incentive(pool: QuickSwapV3AlgebraPoolContract) -> str:  # noqa: D103
    yield pool.activeIncentive()


@pytest.mark.unit
def test__active_incentive__must_be_str(active_incentive: str):  # noqa: D103
    assert isinstance(active_incentive, str)


@pytest.mark.unit
def test__active_incentive__must_be_equal_to_address(active_incentive: str):  # noqa: D103
    assert active_incentive == "0x49e2597DA21ebbB9Bc4D48345712b619374b24c0"


@pytest.mark.unit
def test__active_incentive__must_be_address(active_incentive: str):  # noqa: D103
    assert Web3.is_address(active_incentive) is True
