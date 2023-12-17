import pytest
from raffaelo_uniswap_v3.pool.contract import UniSwapV3PoolContract


@pytest.fixture(scope="module")
def seconds_agos() -> list:  # noqa: D103
    yield [2]


@pytest.fixture(scope="module")
def observe(pool: UniSwapV3PoolContract, seconds_agos: list) -> list:  # noqa: D103
    yield pool.observe(secondsAgos=seconds_agos)


@pytest.mark.unit
def test__observe__must_be_list(observe: list):  # noqa: D103
    assert isinstance(observe, list)


@pytest.mark.unit
def test__observe__must_be_equal_to_2(observe: list):  # noqa: D103
    assert len(observe) == 2


@pytest.mark.unit
def test__observe_tick_cumulatives__must_be_int(observe: list):  # noqa: D103
    assert isinstance(observe[0][0], int)


@pytest.mark.unit
def test__observe_tick_cumulatives__must_be_positive(observe: list):  # noqa: D103
    assert observe[0][0] >= 0


@pytest.mark.unit
def test__observe_seconds_per_liquidity_cumulative_x128s__must_be_int(observe: list):  # noqa: D103
    assert isinstance(observe[1][0], int)


@pytest.mark.unit
def test__observe_seconds_per_liquidity_cumulative_x128s__must_be_positive(observe: list):  # noqa: D103
    assert observe[1][0] >= 0
