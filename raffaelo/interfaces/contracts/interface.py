from abc import ABC
from typing import Any, Dict, Generic, Optional, final, overload

from web3 import Web3
from web3.eth import Eth
from web3.exceptions import CannotHandleRequest, ValidationError

from raffaelo.typings.providers.typing import ProviderType


class iCBC(ABC):
    """iCBC is an abstract base class representing an interface for interacting with a generic blockchain contract.

    Attributes
    ----------
        _ABI (str): The ABI (Application Binary Interface) of the contract.
        _address (str): The address of the contract.
        _provider (Generic[ProviderType]): The provider used to connect to the blockchain.
        _contract (Eth.contract): The Ethereum contract instance.
    """

    _ABI = None

    def __init__(self, address: str, provider: Generic[ProviderType]) -> None:
        """Initializes the iCBC instance with the provided address and provider.

        Args:
        ----
            address (str): The address of the contract.
            provider (Generic[ProviderType]): The provider used to connect to the blockchain.
        """
        self._address = address
        self._provider = provider

        self._contract = self.contract = None

    @property
    def contract(self) -> Eth.contract:
        """Gets the Ethereum contract instance.

        Returns
        -------
            Eth.contract: The Ethereum contract instance.
        """
        return self._contract

    @contract.setter
    def contract(self, *args, **kwargs) -> None:
        """Sets the Ethereum contract instance.

        Args:
        ----
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        self._contract = (
            self.builder.build(key="address", value=self._address)
            .build(key="provider", value=self._provider)
            .connect()
            .construct()
        )

    @property
    def provider(self):
        """Gets the provider used to connect to the blockchain.

        Returns
        -------
            Generic[ProviderType]: The provider used to connect to the blockchain.
        """
        return self._provider

    @property
    def node(self):
        """Gets the underlying provider's node.

        Returns
        -------
            Any: The underlying provider's node.
        """
        return self.provider.provider

    class Builder:
        """Builder is a nested class within iCBC for building iCBC instances with validated parameters."""

        def __init__(self, abi: str) -> None:
            """Initializes the Builder instance with the provided ABI.

            Args:
            ----
                abi (str): The ABI (Application Binary Interface) of the contract.
            """
            self._options: Dict[str, Any] = dict()

            self._abi: str = abi

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
            params: Optional[Dict[str, Any]] = None,
        ) -> "iCBC.Builder":
            """Builds the iCBC instance with validated parameters.

            Args:
            ----
                key (Optional[str]): The key of the parameter.
                value (Optional[str]): The value of the parameter.
                params (Optional[Dict[str, Any]]): Additional parameters as a dictionary.

            Returns:
            -------
                iCBC.Builder: The Builder instance.
            """

            def validate(k: str, v: Any) -> None:
                if k == "address":
                    if not Web3.is_address(value=v):
                        raise ValidationError("Invalid address")
                elif k == "provider":
                    if not v.provider.is_connected():
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
        def connect(self) -> "iCBC.Builder":
            """Connects the iCBC instance by validating and converting the address to a checksum address.

            Returns
            -------
                iCBC.Builder: The Builder instance.
            """
            if self._options.get("address"):
                self._options["address"] = Web3.to_checksum_address(
                    value=self._options.get("address"),
                )
            return self

        @final
        def construct(self) -> Eth.contract:
            """Constructs the Ethereum contract instance.

            Returns
            -------
                Eth.contract: The Ethereum contract instance.
            """
            return Web3(provider=self._options["provider"].provider).eth.contract(
                address=self._options["address"],
                abi=self._abi,
            )

    @property
    def builder(self) -> Builder:
        """Gets the Builder instance for building iCBC instances.

        Returns
        -------
            iCBC.Builder: The Builder instance.
        """
        return self.Builder(abi=self._ABI)
