from typing import Dict, Any, Optional, Generic, overload, final
from abc import ABC

from web3 import Web3
from web3.exceptions import ValidationError, CannotHandleRequest

from raffaelo.typings.providers.typing import ProviderType


class iCBC(ABC):
    _ABI = None

    def __init__(self, address: str, provider: Generic[ProviderType]) -> None:
        self._address = address
        self._provider = provider

        self._contract = self.contract = None

    def __call__(self, *args, **kwargs):
        return self.contract

    @property
    def contract(self):
        return self._contract

    @contract.setter
    def contract(self, *args, **kwargs):
        self._contract = self.builder.build(key='address', value=self.address).build(key='provider', value=self.provider).connect().construct()

    @property
    def address(self):
        return self._address

    @property
    def provider(self):
        return self._provider

    @property
    def abi(self):
        return self._ABI

    class Builder:
        def __init__(self, abi: str) -> None:
            self._options: Dict[str, Any] = dict()

            self._abi: str = abi

        @property
        def abi(self):
            return self._abi

        @overload
        def build(self, params: Dict[str, Any]) -> "iCBC.Builder":
            ...

        @overload
        def build(self, key: str, value: Any) -> "iCBC.Builder":
            ...

        @final
        def build(
                self,
                key: Optional[str] = None,
                value: Optional[str] = None,
                params: Optional[Dict[str, Any]] = None
        ) -> "iCBC.Builder":

            def validate(k: str, v: Any) -> None:
                if k == 'address':
                    if not Web3.isAddress(value=v):
                        raise ValidationError("Invalid address")
                elif k == 'provider':
                    if not v().isConnected():
                        raise CannotHandleRequest("Provider is down")

            if isinstance(params, dict):
                for k, v in params.items():
                    validate(k=k, v=v)
                    self._options[k] = v
            elif isinstance(key, str):
                validate(k=key, v=value)
                self._options[key] = value
            return self

        @final
        def connect(self):
            if self._options.get('address'):
                self._options['address'] = Web3.toChecksumAddress(value=self._options.get('address'))
            return self

        @final
        def construct(self):
            return Web3(provider=self._options['provider']()).eth.contract(address=self._options['address'], abi=self.abi)

    @property
    def builder(self) -> Builder:
        return self.Builder(abi=self.abi)
