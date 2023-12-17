import pytest
from raffaelo_quickswap_v3.pool.contract import QuickSwapV3AlgebraPoolContract


@pytest.fixture(scope="module")
def tick_spacing(pool: QuickSwapV3AlgebraPoolContract) -> int:  # noqa: D103
    yield pool.tickSpacing()


@pytest.mark.unit
def test__tick_spacing__must_be_int(tick_spacing: int):  # noqa: D103
    assert isinstance(tick_spacing, int)


@pytest.mark.unit
def test__tick_spacing__must_be_positive(tick_spacing: int):  # noqa: D103
    assert tick_spacing >= 0
