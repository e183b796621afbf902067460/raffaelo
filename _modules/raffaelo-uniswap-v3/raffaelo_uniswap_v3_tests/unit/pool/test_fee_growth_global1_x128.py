import pytest
from raffaelo_uniswap_v3.pool.contract import UniSwapV3PoolContract


@pytest.fixture(scope="module")
def fee_growth_global1_x128(pool: UniSwapV3PoolContract) -> int:  # noqa: D103
    yield pool.feeGrowthGlobal1X128()


@pytest.mark.unit
def test__fee_growth_global1_x128__must_be_int(fee_growth_global1_x128: int):  # noqa: D103
    assert isinstance(fee_growth_global1_x128, int)


@pytest.mark.unit
def test__fee_growth_global1_x128__must_be_positive(fee_growth_global1_x128: int):  # noqa: D103
    assert fee_growth_global1_x128 >= 0
