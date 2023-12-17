import pytest
from raffaelo_quickswap_v3.pool.contract import QuickSwapV3AlgebraPoolContract


@pytest.fixture(scope="module")
def i() -> int:  # noqa: D103
    yield 0


@pytest.fixture(scope="module")
def tick_table(pool: QuickSwapV3AlgebraPoolContract, i: int) -> int:  # noqa: D103
    yield pool.tickTable(i=i)


@pytest.mark.unit
def test__tick_table__must_be_int(tick_table: int):  # noqa: D103
    assert isinstance(tick_table, int)


@pytest.mark.unit
def test__tick_table__must_be_positive(tick_table: int):  # noqa: D103
    assert tick_table >= 0
