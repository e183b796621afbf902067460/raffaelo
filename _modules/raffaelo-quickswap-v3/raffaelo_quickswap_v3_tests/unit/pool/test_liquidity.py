import pytest
from raffaelo_quickswap_v3.pool.contract import QuickSwapV3AlgebraPoolContract


@pytest.fixture(scope="module")
def liquidity(pool: QuickSwapV3AlgebraPoolContract) -> int:  # noqa: D103
    yield pool.liquidity()


@pytest.mark.unit
def test__liquidity__must_be_int(liquidity: int):  # noqa: D103
    assert isinstance(liquidity, int)


@pytest.mark.unit
def test__liquidity__must_be_positive(liquidity: int):  # noqa: D103
    assert liquidity >= 0
