import pytest
from raffaelo_quickswap_v3.pool.contract import QuickSwapV3AlgebraPoolContract


@pytest.fixture(scope="module")
def i() -> int:  # noqa: D103
    yield 0


@pytest.fixture(scope="module")
def ticks(pool: QuickSwapV3AlgebraPoolContract, i: int) -> list:  # noqa: D103
    yield pool.ticks(i=i)


@pytest.mark.unit
def test__ticks__must_be_list(ticks: list):  # noqa: D103
    assert isinstance(ticks, list)


@pytest.mark.unit
def test__ticks__must_be_equal_to_8(ticks: list):  # noqa: D103
    assert len(ticks) == 8


@pytest.mark.unit
def test__ticks_liquidity_total__must_be_int(ticks: list):  # noqa: D103
    assert isinstance(ticks[0], int)


@pytest.mark.unit
def test__ticks_liquidity_total__must_be_positive(ticks: list):  # noqa: D103
    assert ticks[0] >= 0


@pytest.mark.unit
def test__ticks_liquidity_delta__must_be_int(ticks: list):  # noqa: D103
    assert isinstance(ticks[1], int)


@pytest.mark.unit
def test__ticks_liquidity_delta__must_be_positive(ticks: list):  # noqa: D103
    assert ticks[1] >= 0


@pytest.mark.unit
def test__ticks_outer_fee_growth0_token__must_be_int(ticks: list):  # noqa: D103
    assert isinstance(ticks[2], int)


@pytest.mark.unit
def test__ticks_outer_fee_growth0_token__must_be_positive(ticks: list):  # noqa: D103
    assert ticks[2] >= 0


@pytest.mark.unit
def test__ticks_outer_fee_growth1_token__must_be_int(ticks: list):  # noqa: D103
    assert isinstance(ticks[3], int)


@pytest.mark.unit
def test__ticks_outer_fee_growth1_token__must_be_positive(ticks: list):  # noqa: D103
    assert ticks[3] >= 0


@pytest.mark.unit
def test__ticks_outer_tick_cumulative__must_be_int(ticks: list):  # noqa: D103
    assert isinstance(ticks[4], int)


@pytest.mark.unit
def test__ticks_outer_tick_cumulative__must_be_positive(ticks: list):  # noqa: D103
    assert ticks[4] >= 0


@pytest.mark.unit
def test__ticks_outer_seconds_per_liquidity__must_be_int(ticks: list):  # noqa: D103
    assert isinstance(ticks[5], int)


@pytest.mark.unit
def test__ticks_outer_seconds_per_liquidity__must_be_positive(ticks: list):  # noqa: D103
    assert ticks[5] >= 0


@pytest.mark.unit
def test__ticks_outer_seconds_spent__must_be_int(ticks: list):  # noqa: D103
    assert isinstance(ticks[6], int)


@pytest.mark.unit
def test__ticks_outer_seconds_spent__must_be_positive(ticks: list):  # noqa: D103
    assert ticks[6] >= 0


@pytest.mark.unit
def test__ticks_initialized__must_be_bool(ticks: list):  # noqa: D103
    assert isinstance(ticks[7], bool)


@pytest.mark.unit
def test__ticks_initialized__must_be_false(ticks: list):  # noqa: D103
    assert ticks[7] is False
