import pytest
from raffaelo_uniswap_v3.pool.contract import UniSwapV3PoolContract


@pytest.fixture(scope="module")
def i() -> int:  # noqa: D103
    yield 0


@pytest.fixture(scope="module")
def tick_bitmap(pool: UniSwapV3PoolContract, i: int) -> int:  # noqa: D103
    yield pool.tickBitmap(i=i)


@pytest.mark.unit
def test__tick_bitmap__must_be_int(tick_bitmap: int):  # noqa: D103
    assert isinstance(tick_bitmap, int)


@pytest.mark.unit
def test__tick_bitmap__must_be_positive(tick_bitmap: int):  # noqa: D103
    assert tick_bitmap >= 0
