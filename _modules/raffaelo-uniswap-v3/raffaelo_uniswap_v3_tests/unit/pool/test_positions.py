import pytest
from raffaelo_uniswap_v3.pool.contract import UniSwapV3PoolContract

from raffaelo.utils import string_to_bytes32


@pytest.fixture(scope="module")
def factory(pool: UniSwapV3PoolContract) -> str:  # noqa: D103
    yield pool.factory()


@pytest.fixture(scope="module")
def positions(pool: UniSwapV3PoolContract, factory: str) -> list:  # noqa: D103
    yield pool.positions(i=string_to_bytes32(factory))


@pytest.mark.unit
def test__positions__must_be_list(positions: list):  # noqa: D103
    assert isinstance(positions, list)


@pytest.mark.unit
def test__positions__must_be_equal_to_5(positions: list):  # noqa: D103
    assert len(positions) == 5


@pytest.mark.unit
def test__positions_liquidity__must_be_int(positions: list):  # noqa: D103
    assert isinstance(positions[0], int)


@pytest.mark.unit
def test__positions_liquidity__must_be_equal_to_0(positions: list):  # noqa: D103
    assert positions[0] == 0


@pytest.mark.unit
def test__positions_fee_growth_inside0_last_x128__must_be_int(positions: list):  # noqa: D103
    assert isinstance(positions[1], int)


@pytest.mark.unit
def test__positions_fee_growth_inside0_last_x128__must_be_equal_to_0(positions: list):  # noqa: D103
    assert positions[1] == 0


@pytest.mark.unit
def test__positions_fee_growth_inside1_last_x128__must_be_int(positions: list):  # noqa: D103
    assert isinstance(positions[2], int)


@pytest.mark.unit
def test__positions_fee_growth_inside1_last_x128__must_be_equal_to_0(positions: list):  # noqa: D103
    assert positions[2] == 0


@pytest.mark.unit
def test__positions_tokens_owed0__must_be_int(positions: list):  # noqa: D103
    assert isinstance(positions[3], int)


@pytest.mark.unit
def test__positions_tokens_owed0__must_be_equal_to_0(positions: list):  # noqa: D103
    assert positions[3] == 0


@pytest.mark.unit
def test__positions_tokens_owed1__must_be_int(positions: list):  # noqa: D103
    assert isinstance(positions[4], int)


@pytest.mark.unit
def test__positions_tokens_owed1__must_be_equal_to_0(positions: list):  # noqa: D103
    assert positions[4] == 0
