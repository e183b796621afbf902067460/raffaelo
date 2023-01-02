from raffaelo.interfaces.providers.interface import iCBP


class HTTPProvider(iCBP):
    def __init__(self, uri: str) -> None:
        super().__init__(protocol='http', uri=uri)
