import pytest
from raffaelo_uniswap_v3.pool.contract import UniSwapV3PoolContract


@pytest.fixture(scope="module")
def i() -> int:  # noqa: D103
    yield 0


@pytest.fixture(scope="module")
def ticks(pool: UniSwapV3PoolContract, i: int) -> list:  # noqa: D103
    yield pool.ticks(i=i)


@pytest.mark.unit
def test__ticks__must_be_list(ticks: list):  # noqa: D103
    assert isinstance(ticks, list)


@pytest.mark.unit
def test__ticks__must_be_equal_to_8(ticks: list):  # noqa: D103
    assert len(ticks) == 8


@pytest.mark.unit
def test__ticks_liquidity_gross__must_be_int(ticks: list):  # noqa: D103
    assert isinstance(ticks[0], int)


@pytest.mark.unit
def test__ticks_liquidity_gross__must_be_positive(ticks: list):  # noqa: D103
    assert ticks[0] >= 0


@pytest.mark.unit
def test__ticks_liquidity_net__must_be_int(ticks: list):  # noqa: D103
    assert isinstance(ticks[1], int)


@pytest.mark.unit
def test__ticks_liquidity_net__must_be_positive(ticks: list):  # noqa: D103
    assert ticks[1] >= 0


@pytest.mark.unit
def test__ticks_fee_growth_outside0_x128__must_be_int(ticks: list):  # noqa: D103
    assert isinstance(ticks[2], int)


@pytest.mark.unit
def test__ticks_fee_growth_outside0_x128__must_be_positive(ticks: list):  # noqa: D103
    assert ticks[2] >= 0


@pytest.mark.unit
def test__ticks_fee_growth_outside1_x128__must_be_int(ticks: list):  # noqa: D103
    assert isinstance(ticks[3], int)


@pytest.mark.unit
def test__ticks_fee_growth_outside1_x128__must_be_positive(ticks: list):  # noqa: D103
    assert ticks[3] >= 0


@pytest.mark.unit
def test__ticks_tick_cumulative_outside__must_be_int(ticks: list):  # noqa: D103
    assert isinstance(ticks[4], int)


@pytest.mark.unit
def test__ticks_tick_cumulative_outside__must_be_positive(ticks: list):  # noqa: D103
    assert ticks[4] >= 0


@pytest.mark.unit
def test__ticks_seconds_per_liquidity_outside_x128__must_be_int(ticks: list):  # noqa: D103
    assert isinstance(ticks[5], int)


@pytest.mark.unit
def test__ticks_seconds_per_liquidity_outside_x128__must_be_positive(ticks: list):  # noqa: D103
    assert ticks[5] >= 0


@pytest.mark.unit
def test__ticks_seconds_outside__must_be_int(ticks: list):  # noqa: D103
    assert isinstance(ticks[6], int)


@pytest.mark.unit
def test__ticks_seconds_outside__must_be_positive(ticks: list):  # noqa: D103
    assert ticks[6] >= 0


@pytest.mark.unit
def test__ticks_initialized_status__must_be_bool(ticks: list):  # noqa: D103
    assert isinstance(ticks[7], bool)


@pytest.mark.unit
def test__ticks_initialized_status__must_be_true(ticks: list):  # noqa: D103
    assert ticks[7] is True
