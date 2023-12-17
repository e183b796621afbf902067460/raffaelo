import pytest
from raffaelo_uniswap_v3.pool.contract import UniSwapV3PoolContract


@pytest.fixture(scope="module")
def slot0(pool: UniSwapV3PoolContract) -> list:  # noqa: D103
    yield pool.slot0()


@pytest.mark.unit
def test__slot0__must_be_list(slot0: list):  # noqa: D103
    assert isinstance(slot0, list)


@pytest.mark.unit
def test__slot0__must_be_equal_to_7(slot0: list):  # noqa: D103
    assert len(slot0) == 7


@pytest.mark.unit
def test__slot0_sqrt_price_x96__must_be_int(slot0: list):  # noqa: D103
    assert isinstance(slot0[0], int)


@pytest.mark.unit
def test__slot0_sqrt_price_x96__must_be_positive(slot0: list):  # noqa: D103
    assert slot0[0] >= 0


@pytest.mark.unit
def test__slot0_tick__must_be_int(slot0: list):  # noqa: D103
    assert isinstance(slot0[1], int)


@pytest.mark.unit
def test__slot0_tick__must_be_positive(slot0: list):  # noqa: D103
    assert slot0[1] >= 0


@pytest.mark.unit
def test__slot0_observation_index__must_be_int(slot0: list):  # noqa: D103
    assert isinstance(slot0[2], int)


@pytest.mark.unit
def test__slot0_observation_index__must_be_positive(slot0: list):  # noqa: D103
    assert slot0[2] >= 0


@pytest.mark.unit
def test__slot0_observation_cardinality__must_be_int(slot0: list):  # noqa: D103
    assert isinstance(slot0[3], int)


@pytest.mark.unit
def test__slot0_observation_cardinality__must_be_positive(slot0: list):  # noqa: D103
    assert slot0[3] >= 0


@pytest.mark.unit
def test__slot0_observation_cardinality_next__must_be_int(slot0: list):  # noqa: D103
    assert isinstance(slot0[4], int)


@pytest.mark.unit
def test__slot0_observation_cardinality_next__must_be_positive(slot0: list):  # noqa: D103
    assert slot0[4] >= 0


@pytest.mark.unit
def test__slot0_fee_protocol__must_be_int(slot0: list):  # noqa: D103
    assert isinstance(slot0[5], int)


@pytest.mark.unit
def test__slot0_fee_protocol__must_be_positive(slot0: list):  # noqa: D103
    assert slot0[5] >= 0


@pytest.mark.unit
def test__slot0_unlocked_status__must_be_bool(slot0: list):  # noqa: D103
    assert isinstance(slot0[6], bool)


@pytest.mark.unit
def test__slot0_unlocked_status__must_be_true(slot0: list):  # noqa: D103
    assert slot0[6] is True
