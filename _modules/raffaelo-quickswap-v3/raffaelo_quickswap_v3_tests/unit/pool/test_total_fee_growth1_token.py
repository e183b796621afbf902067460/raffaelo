import pytest
from raffaelo_quickswap_v3.pool.contract import QuickSwapV3AlgebraPoolContract


@pytest.fixture(scope="module")
def total_fee_growth1_token(pool: QuickSwapV3AlgebraPoolContract) -> int:  # noqa: D103
    yield pool.totalFeeGrowth0Token()


@pytest.mark.unit
def test__total_fee_growth1_token__must_be_int(total_fee_growth1_token: int):  # noqa: D103
    assert isinstance(total_fee_growth1_token, int)


@pytest.mark.unit
def test__total_fee_growth1_token__must_be_positive(total_fee_growth1_token: int):  # noqa: D103
    assert total_fee_growth1_token >= 0
