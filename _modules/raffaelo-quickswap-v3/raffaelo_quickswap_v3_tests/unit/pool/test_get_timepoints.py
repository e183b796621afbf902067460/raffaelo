import pytest
from raffaelo_quickswap_v3.pool.contract import QuickSwapV3AlgebraPoolContract


@pytest.fixture(scope="module")
def seconds_agos() -> list:  # noqa: D103
    yield [2]


@pytest.fixture(scope="module")
def get_timepoints(pool: QuickSwapV3AlgebraPoolContract, seconds_agos: list) -> list:  # noqa: D103
    yield pool.getTimepoints(secondsAgos=seconds_agos)


@pytest.mark.unit
def test__get_timepoints__must_be_list(get_timepoints: list):  # noqa: D103
    assert isinstance(get_timepoints, list)


@pytest.mark.unit
def test__get_timepoints__must_be_equal_to_4(get_timepoints: list):  # noqa: D103
    assert len(get_timepoints) == 4


@pytest.mark.unit
def test__get_timepoints_tick_cumulatives__must_be_int(get_timepoints: list):  # noqa: D103
    assert isinstance(get_timepoints[0][0], int)


@pytest.mark.unit
def test__get_timepoints_tick_cumulatives__must_be_negative(get_timepoints: list):  # noqa: D103
    assert get_timepoints[0][0] < 0


@pytest.mark.unit
def test__get_timepoints_seconds_per_liquidity_cumulatives__must_be_int(get_timepoints: list):  # noqa: D103
    assert isinstance(get_timepoints[1][0], int)


@pytest.mark.unit
def test__get_timepoints_seconds_per_liquidity_cumulatives__must_be_positive(get_timepoints: list):  # noqa: D103
    assert get_timepoints[1][0] >= 0


@pytest.mark.unit
def test__get_timepoints_volatility_cumulatives__must_be_int(get_timepoints: list):  # noqa: D103
    assert isinstance(get_timepoints[2][0], int)


@pytest.mark.unit
def test__get_timepoints_volatility_cumulatives__must_be_positive(get_timepoints: list):  # noqa: D103
    assert get_timepoints[2][0] >= 0


@pytest.mark.unit
def test__get_timepoints_volume_per_avg_liquiditys__must_be_int(get_timepoints: list):  # noqa: D103
    assert isinstance(get_timepoints[3][0], int)


@pytest.mark.unit
def test__get_timepoints_volume_per_avg_liquiditys__must_be_positive(get_timepoints: list):  # noqa: D103
    assert get_timepoints[3][0] >= 0
