import pytest
from raffaelo_uniswap_v3.pool.contract import UniSwapV3PoolContract


@pytest.fixture(scope="module")
def max_liquidity_per_tick(pool: UniSwapV3PoolContract) -> int:  # noqa: D103
    yield pool.maxLiquidityPerTick()


@pytest.mark.unit
def test__max_liquidity_per_tick__must_be_int(max_liquidity_per_tick: int):  # noqa: D103
    assert isinstance(max_liquidity_per_tick, int)


@pytest.mark.unit
def test__max_liquidity_per_tick__must_be_positive(max_liquidity_per_tick: int):  # noqa: D103
    assert max_liquidity_per_tick >= 0
