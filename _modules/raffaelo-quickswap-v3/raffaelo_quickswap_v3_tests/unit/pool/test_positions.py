import pytest
from raffaelo_quickswap_v3.pool.contract import QuickSwapV3AlgebraPoolContract

from raffaelo.utils import string_to_bytes32


@pytest.fixture(scope="module")
def factory(pool: QuickSwapV3AlgebraPoolContract) -> str:  # noqa: D103
    yield pool.factory()


@pytest.fixture(scope="module")
def positions(pool: QuickSwapV3AlgebraPoolContract, factory: str) -> list:  # noqa: D103
    yield pool.positions(i=string_to_bytes32(factory))


@pytest.mark.unit
def test__positions__must_be_list(positions: list):  # noqa: D103
    assert isinstance(positions, list)


@pytest.mark.unit
def test__positions__must_be_equal_to_6(positions: list):  # noqa: D103
    assert len(positions) == 6


@pytest.mark.unit
def test__positions_liquidity__must_be_int(positions: list):  # noqa: D103
    assert isinstance(positions[0], int)


@pytest.mark.unit
def test__positions_liquidity__must_be_equal_to_0(positions: list):  # noqa: D103
    assert positions[0] == 0


@pytest.mark.unit
def test__positions_last_liquidity_add_timestamp__must_be_int(positions: list):  # noqa: D103
    assert isinstance(positions[1], int)


@pytest.mark.unit
def test__positions_last_liquidity_add_timestamp__must_be_equal_to_0(positions: list):  # noqa: D103
    assert positions[1] == 0


@pytest.mark.unit
def test__positions_inner_fee_growth0_token__must_be_int(positions: list):  # noqa: D103
    assert isinstance(positions[2], int)


@pytest.mark.unit
def test__positions_inner_fee_growth0_token__must_be_equal_to_0(positions: list):  # noqa: D103
    assert positions[2] == 0


@pytest.mark.unit
def test__positions_inner_fee_growth1_token__must_be_int(positions: list):  # noqa: D103
    assert isinstance(positions[3], int)


@pytest.mark.unit
def test__positions_inner_fee_growth1_token__must_be_equal_to_0(positions: list):  # noqa: D103
    assert positions[3] == 0


@pytest.mark.unit
def test__positions_fees0__must_be_int(positions: list):  # noqa: D103
    assert isinstance(positions[4], int)


@pytest.mark.unit
def test__positions_fees0__must_be_equal_to_0(positions: list):  # noqa: D103
    assert positions[4] == 0


@pytest.mark.unit
def test__positions_fees1__must_be_int(positions: list):  # noqa: D103
    assert isinstance(positions[5], int)


@pytest.mark.unit
def test__positions_fees1__must_be_equal_to_0(positions: list):  # noqa: D103
    assert positions[5] == 0
