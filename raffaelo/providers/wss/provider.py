from raffaelo.interfaces.providers.interface import iCBP


class WSSProvider(iCBP):
    """WSSProvider is a concrete implementation of the iCBP interface for WebSocket-based blockchain providers.

    Attributes
    ----------
        _uri (str): The URI of the WebSocket blockchain provider.
    """

    def __init__(self, uri: str) -> None:
        """Initializes the WSSProvider instance with the provided URI.

        Args:
        ----
            uri (str): The URI of the WebSocket blockchain provider.
        """
        super().__init__(protocol="wss", uri=uri)
