import pytest
from raffaelo_uniswap_v3.pool.contract import UniSwapV3PoolContract

from raffaelo.contracts.erc20.contract import ERC20TokenContract


@pytest.fixture(scope="module")
def token0(pool: UniSwapV3PoolContract) -> ERC20TokenContract:  # noqa: D103
    yield pool.token0()


@pytest.mark.unit
def test__token0__must_be_erc20(token0: ERC20TokenContract):  # noqa: D103
    assert isinstance(token0, ERC20TokenContract)
