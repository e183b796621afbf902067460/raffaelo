from typing import final
import datetime
from typing import Any, Optional

import requests

from web3.types import HexBytes
from web3.datastructures import AttributeDict


class EthereumEVM(object):

    _API_ENDPOINT = 'https://api.etherscan.io/api'

    def __init__(self, api_key: str) -> None:
        self._api_key = api_key

    def __str__(self) -> str:
        return __class__.__name__

    @property
    def api_key(self) -> str:
        return self._api_key

    @final
    def __r(self, q: str) -> Optional[Any]:
        response = requests.get(f"{self._API_ENDPOINT}?{q}&apikey={self.api_key}").json()
        if response['status'] == '1':
            return response['result']

    @final
    def get_block_no_by_time(self, ts: int) -> str:
        return self.__r(q=f'module=block&action=getblocknobytime&timestamp={ts}&closest=before')

    @staticmethod
    def __serialize_logs_to_web3(logs: list) -> list:
        attrs = list()
        for log in logs:
            log['topics'] = [HexBytes(topic) for topic in log['topics']]
            log['data'] = HexBytes(log['data'])
            log['blockHash'] = HexBytes(log['blockHash'])
            log['transactionHash'] = HexBytes(log['transactionHash'])
            attrs.append(AttributeDict(log))
        return attrs

    @final
    def get_logs(
            self,
            address: str,
            start_time: datetime.datetime, end_time: datetime.datetime,
            start_block: int, end_block: int,
            offset: int = 1000,
            is_to_web3: bool = True
    ) -> list:
        logs, timestamp = list(), end_time.timestamp() - start_time.timestamp()

        parts = int(((end_time - start_time).days * timestamp * 24 + (end_time - start_time).seconds) / timestamp)
        step = int((end_block - start_block) / parts if parts else 1)
        for i in range(parts):
            page = 1
            while True:
                page_logs = self.__r(
                    q=f'module=logs&action=getLogs&address={address}&fromBlock={start_block + i * step}&toBlock={start_block + (i + 1) * step}&page={page}&offset={offset}'
                )
                if not page_logs:
                    break
                logs.extend(page_logs)
                page += 1
                if len(page_logs) < offset:
                    break
        return logs if not is_to_web3 else self.__serialize_logs_to_web3(logs=logs)
