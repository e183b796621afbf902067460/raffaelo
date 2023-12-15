from functools import lru_cache

from raffaelo.interfaces.contracts.interface import iCBC


class ERC20TokenContract(iCBC):
    """ERC20TokenContract represents a contract implementing the iCBC interface.
    It provides methods to interact with an ERC20 token contract on the Ethereum blockchain.

    Attributes
    ----------
        _ABI (str): The ABI (Application Binary Interface) of the contract.
    """

    _ABI = '[{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"}],"name":"approve","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"balance","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transfer","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"},{"name":"_spender","type":"address"}],"name":"allowance","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"payable":true,"stateMutability":"payable","type":"fallback"},{"anonymous":false,"inputs":[{"indexed":true,"name":"owner","type":"address"},{"indexed":true,"name":"spender","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"},{"indexed":true,"name":"to","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Transfer","type":"event"}]'  # noqa: E501

    @lru_cache
    def name(self) -> str:
        """Retrieves the name of the ERC20 token.

        Returns
        -------
            str: The name of the ERC20 token.
        """
        return self.contract.functions.name().call()

    def totalSupply(self) -> int:
        """Retrieves the total supply of the ERC20 token.

        Returns
        -------
            int: The total supply of the ERC20 token.
        """
        return self.contract.functions.totalSupply().call()

    @lru_cache
    def decimals(self) -> int:
        """Retrieves the number of decimal places used by the ERC20 token.

        Returns
        -------
            int: The number of decimal places used by the ERC20 token.
        """
        return self.contract.functions.decimals().call()

    def balanceOf(self, address: str) -> int:
        """Retrieves the balance of the specified address for the ERC20 token.

        Args:
        ----
            address (str): The address for which to retrieve the balance.

        Returns:
        -------
            int: The balance of the specified address for the ERC20 token.
        """
        return self.contract.functions.balanceOf(address).call()

    @lru_cache
    def symbol(self) -> str:
        """Retrieves the symbol (ticker) of the ERC20 token.

        Returns
        -------
            str: The symbol (ticker) of the ERC20 token.
        """
        return self.contract.functions.symbol().call()

    def allowance(self, owner: str, spender: str) -> int:
        """Retrieves the allowance of spending by the specified spender on behalf of the owner.

        Args:
        ----
            owner (str): The owner's address.
            spender (str): The spender's address.

        Returns:
        -------
            int: The allowance of spending by the specified spender on behalf of the owner.
        """
        return self.contract.functions.allowance(owner, spender).call()
