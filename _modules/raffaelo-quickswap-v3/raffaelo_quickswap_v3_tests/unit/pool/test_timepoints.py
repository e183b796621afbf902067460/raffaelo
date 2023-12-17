import pytest
from raffaelo_quickswap_v3.pool.contract import QuickSwapV3AlgebraPoolContract


@pytest.fixture(scope="module")
def i() -> int:  # noqa: D103
    yield 0


@pytest.fixture(scope="module")
def timepoints(pool: QuickSwapV3AlgebraPoolContract, i: int) -> list:  # noqa: D103
    yield pool.timepoints(i=i)


@pytest.mark.unit
def test__timepoints__must_be_list(timepoints: list):  # noqa: D103
    assert isinstance(timepoints, list)


@pytest.mark.unit
def test__timepoints__must_be_equal_to_7(timepoints: list):  # noqa: D103
    assert len(timepoints) == 7


@pytest.mark.unit
def test__timepoints_initialized__must_be_bool(timepoints: list):  # noqa: D103
    assert isinstance(timepoints[0], bool)


@pytest.mark.unit
def test__timepoints_initialized__must_be_true(timepoints: list):  # noqa: D103
    assert timepoints[0] is True


@pytest.mark.unit
def test__timepoints_block_timestamp__must_be_int(timepoints: list):  # noqa: D103
    assert isinstance(timepoints[1], int)


@pytest.mark.unit
def test__timepoints_block_timestamp__must_be_positive(timepoints: list):  # noqa: D103
    assert timepoints[1] >= 0


@pytest.mark.unit
def test__timepoints_tick_cumulative__must_be_int(timepoints: list):  # noqa: D103
    assert isinstance(timepoints[2], int)


@pytest.mark.unit
def test__timepoints_tick_cumulative__must_be_negative(timepoints: list):  # noqa: D103
    assert timepoints[2] < 0


@pytest.mark.unit
def test__timepoints_seconds_per_liquidity_cumulative__must_be_int(timepoints: list):  # noqa: D103
    assert isinstance(timepoints[3], int)


@pytest.mark.unit
def test__timepoints_seconds_per_liquidity_cumulative__must_be_positive(timepoints: list):  # noqa: D103
    assert timepoints[3] >= 0


@pytest.mark.unit
def test__timepoints_volatility_cumulative__must_be_int(timepoints: list):  # noqa: D103
    assert isinstance(timepoints[4], int)


@pytest.mark.unit
def test__timepoints_volatility_cumulative__must_be_positive(timepoints: list):  # noqa: D103
    assert timepoints[4] >= 0


@pytest.mark.unit
def test__timepoints_average_tick__must_be_int(timepoints: list):  # noqa: D103
    assert isinstance(timepoints[5], int)


@pytest.mark.unit
def test__timepoints_average_tick__must_be_negative(timepoints: list):  # noqa: D103
    assert timepoints[5] < 0


@pytest.mark.unit
def test__timepoints_volume_per_liquidity_cumulative__must_be_int(timepoints: list):  # noqa: D103
    assert isinstance(timepoints[6], int)


@pytest.mark.unit
def test__timepoints_volume_per_liquidity_cumulative__must_be_positive(timepoints: list):  # noqa: D103
    assert timepoints[6] >= 0
