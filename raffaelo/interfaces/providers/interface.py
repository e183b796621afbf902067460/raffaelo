from abc import ABC
from typing import Any, Dict, Optional, final, overload
from urllib import parse

from web3.exceptions import ValidationError
from web3.providers.base import BaseProvider
from web3.providers.rpc import HTTPProvider as W3HTTPProvider
from web3.providers.websocket import WebsocketProvider


class iCBP(ABC):
    """iCBP is an abstract base class representing an interface for creating blockchain providers.

    Attributes
    ----------
        _uri (str): The URI of the blockchain provider.
        _protocol (str): The protocol used for communication with the blockchain provider.
        _provider (BaseProvider): The blockchain provider instance.
    """

    def __init__(self, protocol: str, uri: str) -> None:
        """Initializes the iCBP instance with the provided protocol and URI.

        Args:
        ----
            protocol (str): The protocol used for communication with the blockchain provider.
            uri (str): The URI of the blockchain provider.
        """
        self._uri = uri
        self._protocol = protocol

        self._provider = self.provider = None

    @property
    def provider(self) -> BaseProvider:
        """Gets the blockchain provider instance.

        Returns
        -------
            BaseProvider: The blockchain provider instance.
        """
        return self._provider

    @provider.setter
    def provider(self, *args, **kwargs) -> None:
        """Sets the blockchain provider instance.

        Args:
        ----
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        self._provider = (
            self.builder.build(key="protocol", value=self._protocol)
            .build(key="uri", value=self._uri)
            .connect()
            .construct()
        )

    class Builder:
        """Builder is a nested class within iCBP for building iCBP instances with validated parameters."""

        def __init__(self) -> None:
            """Initializes the Builder instance."""

            self._options: Dict[str, Any] = dict()

        @overload
        def build(self, params: Dict[str, Any]) -> "iCBP.Builder":
            ...

        @overload
        def build(self, key: str, value: str) -> "iCBP.Builder":
            ...

        @final
        def build(
            self,
            key: Optional[str] = None,
            value: Optional[str] = None,
            params: Optional[Dict[str, Any]] = None,
        ) -> "iCBP.Builder":
            """Builds the iCBP instance with validated parameters.

            Args:
            ----
                key (Optional[str]): The key of the parameter.
                value (Optional[str]): The value of the parameter.
                params (Optional[Dict[str, Any]]): Additional parameters as a dictionary.

            Returns:
            -------
                iCBP.Builder: The Builder instance.
            """

            def validate(k: str, v: str) -> None:
                if k == "protocol":
                    if v.lower() not in ("http", "https", "websocket", "wss"):
                        raise ValidationError("Invalid protocol")
                elif k == "uri":
                    if parse.urlparse(v).scheme not in ("https", "http", "wss"):
                        raise ValidationError("Invalid uri")

            if isinstance(params, dict):
                for k, v in params.items():
                    validate(k=k, v=v)
                    self._options[k] = v
            elif isinstance(key, str) and isinstance(value, str):
                validate(k=key, v=value)
                self._options[key] = value
            return self

        @final
        def connect(self) -> "iCBP.Builder":
            """Connects the blockchain provider instance by creating an appropriate provider based on the protocol.

            Returns
            -------
                iCBP.Builder: The Builder instance.
            """
            protocol = self._options.get("protocol")
            if protocol in ("http", "https"):
                self._options["provider"] = W3HTTPProvider(
                    endpoint_uri=self._options.get("uri"),
                )
            if protocol in ("wss", "websocket"):
                self._options["provider"] = WebsocketProvider(
                    endpoint_uri=self._options.get("uri"),
                )
            return self

        @final
        def construct(self) -> BaseProvider:
            """Constructs the iCBP instance.

            Returns
            -------
                BaseProvider: The blockchain provider instance.
            """
            return self._options["provider"]

    @property
    def builder(self) -> Builder:
        """Gets the Builder instance for building blockchain provider instances.

        Returns
        -------
            iCBP.Builder: The Builder instance.
        """
        return self.Builder()
