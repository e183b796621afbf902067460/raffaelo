from typing import Dict, Any, Optional, overload, final
from abc import ABC
from urllib import parse

from web3.providers.rpc import HTTPProvider
from web3.providers.base import BaseProvider
from web3.exceptions import ValidationError, CannotHandleRequest


class iCBP(ABC):

    def __init__(self, protocol: str, uri: str) -> None:
        self._uri = uri
        self._protocol = protocol

        self._provider = self.provider = None

    @property
    def provider(self) -> BaseProvider:
        return self._provider

    @provider.setter
    def provider(self, *args, **kwargs) -> None:
        self._provider = self.builder.build(key='protocol', value=self._protocol).build(key='uri', value=self._uri).connect().construct()

    class Builder:
        def __init__(self) -> None:
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
                params: Optional[Dict[str, Any]] = None
        ) -> "iCBP.Builder":

            def validate(k: str, v: str) -> None:
                if k == 'protocol':
                    if v.lower() not in ('http', 'https', 'websocket', 'wss'):
                        raise ValidationError("Invalid protocol")
                elif k == 'uri':
                    if parse.urlparse(v).scheme not in ('https', 'http', 'wss'):
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
            protocol = self._options.get('protocol')
            if protocol in ('http', 'https'):
                http = HTTPProvider(endpoint_uri=self._options.get('uri'))
                if http.isConnected():
                    self._options['provider'] = http
                else:
                    raise CannotHandleRequest("HTTP provider is down")
            if protocol in ('wss', 'websocket'):
                ...
            return self

        @final
        def construct(self) -> BaseProvider:
            return self._options['provider']

    @property
    def builder(self) -> Builder:
        return self.Builder()
