import pytest
from raffaelo_quickswap_v3.pool.contract import QuickSwapV3AlgebraPoolContract

from raffaelo.contracts.erc20.contract import ERC20TokenContract


@pytest.fixture(scope="module")
def token1(pool: QuickSwapV3AlgebraPoolContract) -> ERC20TokenContract:  # noqa: D103
    yield pool.token1()


@pytest.mark.unit
def test__token1__must_be_erc20(token1: ERC20TokenContract):  # noqa: D103
    assert isinstance(token1, ERC20TokenContract)
