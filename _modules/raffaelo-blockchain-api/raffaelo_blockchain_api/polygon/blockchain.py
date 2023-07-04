from raffaelo_blockchain_api.ethereum.blockchain import EthereumEVM


class PolygonEVM(EthereumEVM):

    _API_ENDPOINT = 'https://api.polygonscan.com/api'

    def __str__(self) -> str:
        return __class__.__name__
