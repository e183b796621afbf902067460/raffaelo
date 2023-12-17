import pytest
from raffaelo_uniswap_v3.pool.contract import UniSwapV3PoolContract


@pytest.fixture(scope="module")
def i() -> int:  # noqa: D103
    yield 0


@pytest.fixture(scope="module")
def observations(pool: UniSwapV3PoolContract, i: int) -> list:  # noqa: D103
    yield pool.observations(i=i)


@pytest.mark.unit
def test__observations__must_be_list(observations: list):  # noqa: D103
    assert isinstance(observations, list)


@pytest.mark.unit
def test__observations__must_be_equal_to_4(observations: list):  # noqa: D103
    assert len(observations) == 4


@pytest.mark.unit
def test__observations_block_timestamp__must_be_int(observations: list):  # noqa: D103
    assert isinstance(observations[0], int)


@pytest.mark.unit
def test__observations_block_timestamp__must_be_positive(observations: list):  # noqa: D103
    assert observations[0] >= 0


@pytest.mark.unit
def test__observations_tick_cumulative__must_be_int(observations: list):  # noqa: D103
    assert isinstance(observations[1], int)


@pytest.mark.unit
def test__observations_tick_cumulative__must_be_positive(observations: list):  # noqa: D103
    assert observations[1] >= 0


@pytest.mark.unit
def test__observations_seconds_per_liquidity_cumulative_x128__must_be_int(observations: list):  # noqa: D103
    assert isinstance(observations[2], int)


@pytest.mark.unit
def test__observations_seconds_per_liquidity_cumulative_x128__must_be_positive(observations: list):  # noqa: D103
    assert observations[2] >= 0


@pytest.mark.unit
def test__observations_initialized_status__must_be_bool(observations: list):  # noqa: D103
    assert isinstance(observations[3], bool)


@pytest.mark.unit
def test__observations_initialized_status__must_be_true(observations: list):  # noqa: D103
    assert observations[3] is True
