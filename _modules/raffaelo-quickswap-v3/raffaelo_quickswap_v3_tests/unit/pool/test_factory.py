import pytest
from raffaelo_quickswap_v3.pool.contract import QuickSwapV3AlgebraPoolContract
from web3 import Web3


@pytest.fixture(scope="module")
def factory(pool: QuickSwapV3AlgebraPoolContract) -> str:  # noqa: D103
    yield pool.factory()


@pytest.mark.unit
def test__factory__must_be_str(factory: str):  # noqa: D103
    assert isinstance(factory, str)


@pytest.mark.unit
def test__factory__must_be_equal_to_address(factory: str):  # noqa: D103
    assert factory == "0x411b0fAcC3489691f28ad58c47006AF5E3Ab3A28"


@pytest.mark.unit
def test__factory__must_be_address(factory: str):  # noqa: D103
    assert Web3.is_address(factory) is True
