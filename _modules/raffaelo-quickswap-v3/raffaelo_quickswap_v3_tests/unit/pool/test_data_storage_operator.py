import pytest
from raffaelo_quickswap_v3.pool.contract import QuickSwapV3AlgebraPoolContract
from web3 import Web3


@pytest.fixture(scope="module")
def data_storage_operator(pool: QuickSwapV3AlgebraPoolContract) -> str:  # noqa: D103
    yield pool.dataStorageOperator()


@pytest.mark.unit
def test__data_storage_operator__must_be_str(data_storage_operator: str):  # noqa: D103
    assert isinstance(data_storage_operator, str)


@pytest.mark.unit
def test__data_storage_operator__must_be_equal_to_address(data_storage_operator: str):  # noqa: D103
    assert data_storage_operator == "0x26c0cfB2c884C2bc0eaaA604a22e3aF146A4b1e3"


@pytest.mark.unit
def test__data_storage_operator__must_be_address(data_storage_operator: str):  # noqa: D103
    assert Web3.is_address(data_storage_operator) is True
