import pytest
from raffaelo_uniswap_v3.pool.contract import UniSwapV3PoolContract


@pytest.fixture(scope="module")
def protocol_fees(pool: UniSwapV3PoolContract) -> list:  # noqa: D103
    yield pool.protocolFees()


@pytest.mark.unit
def test__protocol_fees__must_be_list(protocol_fees: list):  # noqa: D103
    assert isinstance(protocol_fees, list)


@pytest.mark.unit
def test__protocol_fees__must_be_equal_to_2(protocol_fees: list):  # noqa: D103
    assert len(protocol_fees) == 2


@pytest.mark.unit
def test__protocol_fees_token0_must_be_int(protocol_fees: list):  # noqa: D103
    assert isinstance(protocol_fees[0], int)


@pytest.mark.unit
def test__protocol_fees_token0__must_be_positive(protocol_fees: list):  # noqa: D103
    assert protocol_fees[0] >= 0


@pytest.mark.unit
def test_protocol_fees_token1__must_be_int(protocol_fees: list):  # noqa: D103
    assert isinstance(protocol_fees[1], int)


@pytest.mark.unit
def test__protocol_fees_token1__must_be_positive(protocol_fees: list):  # noqa: D103
    assert protocol_fees[1] >= 0
