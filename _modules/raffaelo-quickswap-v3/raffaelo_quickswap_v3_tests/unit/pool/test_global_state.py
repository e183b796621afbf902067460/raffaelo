import pytest
from raffaelo_quickswap_v3.pool.contract import QuickSwapV3AlgebraPoolContract


@pytest.fixture(scope="module")
def global_state(pool: QuickSwapV3AlgebraPoolContract) -> list:  # noqa: D103
    yield pool.globalState()


@pytest.mark.unit
def test__global_state__must_be_list(global_state: list):  # noqa: D103
    assert isinstance(global_state, list)


@pytest.mark.unit
def test__global_state__must_be_equal_to_7(global_state: list):  # noqa: D103
    assert len(global_state) == 7


@pytest.mark.unit
def test__global_state_price__must_be_int(global_state: list):  # noqa: D103
    assert isinstance(global_state[0], int)


@pytest.mark.unit
def test__global_state_price__must_be_positive(global_state: list):  # noqa: D103
    assert global_state[0] >= 0


@pytest.mark.unit
def test__global_state_tick__must_be_int(global_state: list):  # noqa: D103
    assert isinstance(global_state[1], int)


@pytest.mark.unit
def test__global_state_tick__must_be_negative(global_state: list):  # noqa: D103
    assert global_state[1] < 0


@pytest.mark.unit
def test__global_state_fee__must_be_int(global_state: list):  # noqa: D103
    assert isinstance(global_state[2], int)


@pytest.mark.unit
def test__global_state_fee__must_be_positive(global_state: list):  # noqa: D103
    assert global_state[2] >= 0


@pytest.mark.unit
def test__global_state_timepoint_index__must_be_int(global_state: list):  # noqa: D103
    assert isinstance(global_state[3], int)


@pytest.mark.unit
def test__global_state_timepoint_index__must_be_positive(global_state: list):  # noqa: D103
    assert global_state[3] >= 0


@pytest.mark.unit
def test__global_state_community_fee_token0__must_be_int(global_state: list):  # noqa: D103
    assert isinstance(global_state[4], int)


@pytest.mark.unit
def test__global_state_community_fee_token0__must_be_positive(global_state: list):  # noqa: D103
    assert global_state[4] >= 0


@pytest.mark.unit
def test__global_state_community_fee_token1__must_be_int(global_state: list):  # noqa: D103
    assert isinstance(global_state[5], int)


@pytest.mark.unit
def test__global_state_community_fee_token1__must_be_positive(global_state: list):  # noqa: D103
    assert global_state[5] >= 0


@pytest.mark.unit
def test__global_state_unlocked__must_be_bool(global_state: list):  # noqa: D103
    assert isinstance(global_state[6], bool)


@pytest.mark.unit
def test__global_state_unlocked__must_be_true(global_state: list):  # noqa: D103
    assert global_state[6] is True
