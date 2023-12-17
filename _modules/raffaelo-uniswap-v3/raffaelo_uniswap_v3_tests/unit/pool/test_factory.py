import pytest
from raffaelo_uniswap_v3.pool.contract import UniSwapV3PoolContract
from web3 import Web3


@pytest.fixture(scope="module")
def factory(pool: UniSwapV3PoolContract) -> str:  # noqa: D103
    yield pool.factory()


@pytest.mark.unit
def test__factory__must_be_str(factory: str):  # noqa: D103
    assert isinstance(factory, str)


@pytest.mark.unit
def test__factory__must_be_equal_to_address(factory: str):  # noqa: D103
    assert factory == "0x1F98431c8aD98523631AE4a59f267346ea31F984"


@pytest.mark.unit
def test__factory__must_be_address(factory: str):  # noqa: D103
    assert Web3.is_address(factory) is True
