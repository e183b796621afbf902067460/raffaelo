from raffaelo.interfaces.providers.interface import iCBP


class WSSProvider(iCBP):
    def __init__(self, uri: str) -> None:
        super().__init__(protocol='wss', uri=uri)
