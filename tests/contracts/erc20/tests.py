import pytest

from raffaelo.contracts.erc20.contract import ERC20TokenContract
from raffaelo.providers.http.provider import HTTPProvider


class TestERC20TokenContract:
    mock = '0x0000000000000000000000000000000000000000'
    address = '0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48'
    provider = HTTPProvider(uri='')

    @classmethod
    def setup_class(cls):
        cls.contract = ERC20TokenContract(address=cls.address, provider=cls.provider)

    def test__name(self):
        assert isinstance(self.contract.name(), str)

    def test__totalSupply(self):
        assert isinstance(self.contract.totalSupply(), int)

    def test__decimals(self):
        assert isinstance(self.contract.decimals(), int)

    def test__balanceOf(self):
        assert isinstance(self.contract.balanceOf(address=self.mock), int)

    def test__symbol(self):
        assert isinstance(self.contract.symbol(), str)

    def test__allowance(self):
        assert isinstance(self.contract.allowance(owner=self.mock, spender=self.mock), int)
