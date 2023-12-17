import pytest
from raffaelo_uniswap_v3.pool.contract import UniSwapV3PoolContract


@pytest.fixture(scope="module")
def liquidity(pool: UniSwapV3PoolContract) -> int:  # noqa: D103
    yield pool.liquidity()


@pytest.mark.unit
def test__liquidity__must_be_int(liquidity: int):  # noqa: D103
    assert isinstance(liquidity, int)


@pytest.mark.unit
def test__liquidity__must_be_positive(liquidity: int):  # noqa: D103
    assert liquidity >= 0
