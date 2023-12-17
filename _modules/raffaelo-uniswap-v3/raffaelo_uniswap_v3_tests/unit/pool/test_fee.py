import pytest
from raffaelo_uniswap_v3.pool.contract import UniSwapV3PoolContract


@pytest.fixture(scope="module")
def fee(pool: UniSwapV3PoolContract) -> int:  # noqa: D103
    yield pool.fee()


@pytest.mark.unit
def test__fee__must_be_int(fee: int):  # noqa: D103
    assert isinstance(fee, int)


@pytest.mark.unit
def test__fee__must_be_positive(fee: int):  # noqa: D103
    assert fee >= 0


@pytest.mark.unit
def test__fee__must_be_equal_to_500(fee):  # noqa: D103
    assert fee == 500
