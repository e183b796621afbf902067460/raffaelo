from raffaelo.interfaces.providers.interface import iCBP


class HTTPProvider(iCBP):
    """HTTPProvider is a concrete implementation of the iCBP interface for HTTP-based blockchain providers.

    Attributes
    ----------
        _uri (str): The URI of the HTTP blockchain provider.
    """

    def __init__(self, uri: str) -> None:
        """Initializes the HTTPProvider instance with the provided URI.

        Args:
        ----
            uri (str): The URI of the HTTP blockchain provider.
        """
        super().__init__(protocol="http", uri=uri)
