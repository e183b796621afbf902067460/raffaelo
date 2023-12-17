import pytest
from raffaelo_quickswap_v3.pool.contract import QuickSwapV3AlgebraPoolContract


@pytest.fixture(scope="module")
def liquidity_cooldown(pool: QuickSwapV3AlgebraPoolContract) -> int:  # noqa: D103
    yield pool.liquidityCooldown()


@pytest.mark.unit
def test__liquidity_cooldown__must_be_int(liquidity_cooldown: int):  # noqa: D103
    assert isinstance(liquidity_cooldown, int)


@pytest.mark.unit
def test__liquidity_cooldown__must_be_positive(liquidity_cooldown: int):  # noqa: D103
    assert liquidity_cooldown >= 0
