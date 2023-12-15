from functools import lru_cache
from typing import List

from raffaelo.contracts.erc20.contract import ERC20TokenContract
from raffaelo.interfaces.contracts.interface import iCBC


class UniSwapV3PoolContract(iCBC):
    """UniSwapV3PoolContract represents a contract implementing the iCBC interface.
    It provides methods to interact with a UniSwap V3 pool on the blockchain.

    Attributes
    ----------
        _ABI (str): The ABI (Application Binary Interface) of the contract.
    """

    _ABI: str = '[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"int24","name":"tickLower","type":"int24"},{"indexed":true,"internalType":"int24","name":"tickUpper","type":"int24"},{"indexed":false,"internalType":"uint128","name":"amount","type":"uint128"},{"indexed":false,"internalType":"uint256","name":"amount0","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1","type":"uint256"}],"name":"Burn","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":false,"internalType":"address","name":"recipient","type":"address"},{"indexed":true,"internalType":"int24","name":"tickLower","type":"int24"},{"indexed":true,"internalType":"int24","name":"tickUpper","type":"int24"},{"indexed":false,"internalType":"uint128","name":"amount0","type":"uint128"},{"indexed":false,"internalType":"uint128","name":"amount1","type":"uint128"}],"name":"Collect","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"sender","type":"address"},{"indexed":true,"internalType":"address","name":"recipient","type":"address"},{"indexed":false,"internalType":"uint128","name":"amount0","type":"uint128"},{"indexed":false,"internalType":"uint128","name":"amount1","type":"uint128"}],"name":"CollectProtocol","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"sender","type":"address"},{"indexed":true,"internalType":"address","name":"recipient","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount0","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"paid0","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"paid1","type":"uint256"}],"name":"Flash","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint16","name":"observationCardinalityNextOld","type":"uint16"},{"indexed":false,"internalType":"uint16","name":"observationCardinalityNextNew","type":"uint16"}],"name":"IncreaseObservationCardinalityNext","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint160","name":"sqrtPriceX96","type":"uint160"},{"indexed":false,"internalType":"int24","name":"tick","type":"int24"}],"name":"Initialize","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"sender","type":"address"},{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"int24","name":"tickLower","type":"int24"},{"indexed":true,"internalType":"int24","name":"tickUpper","type":"int24"},{"indexed":false,"internalType":"uint128","name":"amount","type":"uint128"},{"indexed":false,"internalType":"uint256","name":"amount0","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1","type":"uint256"}],"name":"Mint","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint8","name":"feeProtocol0Old","type":"uint8"},{"indexed":false,"internalType":"uint8","name":"feeProtocol1Old","type":"uint8"},{"indexed":false,"internalType":"uint8","name":"feeProtocol0New","type":"uint8"},{"indexed":false,"internalType":"uint8","name":"feeProtocol1New","type":"uint8"}],"name":"SetFeeProtocol","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"sender","type":"address"},{"indexed":true,"internalType":"address","name":"recipient","type":"address"},{"indexed":false,"internalType":"int256","name":"amount0","type":"int256"},{"indexed":false,"internalType":"int256","name":"amount1","type":"int256"},{"indexed":false,"internalType":"uint160","name":"sqrtPriceX96","type":"uint160"},{"indexed":false,"internalType":"uint128","name":"liquidity","type":"uint128"},{"indexed":false,"internalType":"int24","name":"tick","type":"int24"}],"name":"Swap","type":"event"},{"inputs":[{"internalType":"int24","name":"tickLower","type":"int24"},{"internalType":"int24","name":"tickUpper","type":"int24"},{"internalType":"uint128","name":"amount","type":"uint128"}],"name":"burn","outputs":[{"internalType":"uint256","name":"amount0","type":"uint256"},{"internalType":"uint256","name":"amount1","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"recipient","type":"address"},{"internalType":"int24","name":"tickLower","type":"int24"},{"internalType":"int24","name":"tickUpper","type":"int24"},{"internalType":"uint128","name":"amount0Requested","type":"uint128"},{"internalType":"uint128","name":"amount1Requested","type":"uint128"}],"name":"collect","outputs":[{"internalType":"uint128","name":"amount0","type":"uint128"},{"internalType":"uint128","name":"amount1","type":"uint128"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint128","name":"amount0Requested","type":"uint128"},{"internalType":"uint128","name":"amount1Requested","type":"uint128"}],"name":"collectProtocol","outputs":[{"internalType":"uint128","name":"amount0","type":"uint128"},{"internalType":"uint128","name":"amount1","type":"uint128"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"factory","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"fee","outputs":[{"internalType":"uint24","name":"","type":"uint24"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"feeGrowthGlobal0X128","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"feeGrowthGlobal1X128","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount0","type":"uint256"},{"internalType":"uint256","name":"amount1","type":"uint256"},{"internalType":"bytes","name":"data","type":"bytes"}],"name":"flash","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint16","name":"observationCardinalityNext","type":"uint16"}],"name":"increaseObservationCardinalityNext","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint160","name":"sqrtPriceX96","type":"uint160"}],"name":"initialize","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"liquidity","outputs":[{"internalType":"uint128","name":"","type":"uint128"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"maxLiquidityPerTick","outputs":[{"internalType":"uint128","name":"","type":"uint128"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"recipient","type":"address"},{"internalType":"int24","name":"tickLower","type":"int24"},{"internalType":"int24","name":"tickUpper","type":"int24"},{"internalType":"uint128","name":"amount","type":"uint128"},{"internalType":"bytes","name":"data","type":"bytes"}],"name":"mint","outputs":[{"internalType":"uint256","name":"amount0","type":"uint256"},{"internalType":"uint256","name":"amount1","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"observations","outputs":[{"internalType":"uint32","name":"blockTimestamp","type":"uint32"},{"internalType":"int56","name":"tickCumulative","type":"int56"},{"internalType":"uint160","name":"secondsPerLiquidityCumulativeX128","type":"uint160"},{"internalType":"bool","name":"initialized","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint32[]","name":"secondsAgos","type":"uint32[]"}],"name":"observe","outputs":[{"internalType":"int56[]","name":"tickCumulatives","type":"int56[]"},{"internalType":"uint160[]","name":"secondsPerLiquidityCumulativeX128s","type":"uint160[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"name":"positions","outputs":[{"internalType":"uint128","name":"liquidity","type":"uint128"},{"internalType":"uint256","name":"feeGrowthInside0LastX128","type":"uint256"},{"internalType":"uint256","name":"feeGrowthInside1LastX128","type":"uint256"},{"internalType":"uint128","name":"tokensOwed0","type":"uint128"},{"internalType":"uint128","name":"tokensOwed1","type":"uint128"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"protocolFees","outputs":[{"internalType":"uint128","name":"token0","type":"uint128"},{"internalType":"uint128","name":"token1","type":"uint128"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint8","name":"feeProtocol0","type":"uint8"},{"internalType":"uint8","name":"feeProtocol1","type":"uint8"}],"name":"setFeeProtocol","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"slot0","outputs":[{"internalType":"uint160","name":"sqrtPriceX96","type":"uint160"},{"internalType":"int24","name":"tick","type":"int24"},{"internalType":"uint16","name":"observationIndex","type":"uint16"},{"internalType":"uint16","name":"observationCardinality","type":"uint16"},{"internalType":"uint16","name":"observationCardinalityNext","type":"uint16"},{"internalType":"uint8","name":"feeProtocol","type":"uint8"},{"internalType":"bool","name":"unlocked","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"int24","name":"tickLower","type":"int24"},{"internalType":"int24","name":"tickUpper","type":"int24"}],"name":"snapshotCumulativesInside","outputs":[{"internalType":"int56","name":"tickCumulativeInside","type":"int56"},{"internalType":"uint160","name":"secondsPerLiquidityInsideX128","type":"uint160"},{"internalType":"uint32","name":"secondsInside","type":"uint32"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"recipient","type":"address"},{"internalType":"bool","name":"zeroForOne","type":"bool"},{"internalType":"int256","name":"amountSpecified","type":"int256"},{"internalType":"uint160","name":"sqrtPriceLimitX96","type":"uint160"},{"internalType":"bytes","name":"data","type":"bytes"}],"name":"swap","outputs":[{"internalType":"int256","name":"amount0","type":"int256"},{"internalType":"int256","name":"amount1","type":"int256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"int16","name":"","type":"int16"}],"name":"tickBitmap","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"tickSpacing","outputs":[{"internalType":"int24","name":"","type":"int24"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"int24","name":"","type":"int24"}],"name":"ticks","outputs":[{"internalType":"uint128","name":"liquidityGross","type":"uint128"},{"internalType":"int128","name":"liquidityNet","type":"int128"},{"internalType":"uint256","name":"feeGrowthOutside0X128","type":"uint256"},{"internalType":"uint256","name":"feeGrowthOutside1X128","type":"uint256"},{"internalType":"int56","name":"tickCumulativeOutside","type":"int56"},{"internalType":"uint160","name":"secondsPerLiquidityOutsideX128","type":"uint160"},{"internalType":"uint32","name":"secondsOutside","type":"uint32"},{"internalType":"bool","name":"initialized","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"token0","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"token1","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"}]'  # noqa: E501

    @lru_cache
    def factory(self) -> str:
        """Retrieves the address of the factory contract that deployed the pool.

        Returns
        -------
            str: The address of the factory contract.
        """
        return self.contract.functions.factory().call()

    @lru_cache
    def fee(self) -> int:
        """Retrieves the fee of the pool.

        Returns
        -------
            int: The fee of the pool.
        """
        return self.contract.functions.fee().call()

    def feeGrowthGlobal0X128(self) -> int:
        """Retrieves the global fee growth for token0.

        Returns
        -------
            int: The global fee growth for token0.
        """
        return self.contract.functions.feeGrowthGlobal0X128().call()

    def feeGrowthGlobal1X128(self) -> int:
        """Retrieves the global fee growth for token1.

        Returns
        -------
            int: The global fee growth for token1.
        """
        return self.contract.functions.feeGrowthGlobal1X128().call()

    def liquidity(self) -> int:
        """Retrieves the current liquidity of the pool.

        Returns
        -------
            int: The current liquidity of the pool.
        """
        return self.contract.functions.liquidity().call()

    def maxLiquidityPerTick(self) -> int:
        """Retrieves the maximum liquidity that can be added per tick.

        Returns
        -------
            int: The maximum liquidity that can be added per tick.
        """
        return self.contract.functions.maxLiquidityPerTick().call()

    def observations(self, i: int) -> list:
        """Retrieves observation-related data for a specified index.

        Args:
        ----
            i (int): The index for which to retrieve observation data.

        Returns:
        -------
            list: A list containing blockTimestamp, tickCumulative, secondsPerLiquidityCumulativeX128,
                  and initialized status.
        """
        return self.contract.functions.observations(i).call()

    def observe(self, secondsAgos: List[int]) -> list:
        """Observes data for the specified time intervals.

        Args:
        ----
            secondsAgos (List[int]): List of time intervals to observe data for.

        Returns:
        -------
            list: A list containing tickCumulatives and secondsPerLiquidityCumulativeX128s.
        """
        return self.contract.functions.observe(secondsAgos).call()

    def positions(self, i: bytes) -> list:
        """Retrieves position-related data for a given index.

        Args:
        ----
            i (bytes): The index for which to retrieve position data.

        Returns:
        -------
            list: A list containing liquidity, feeGrowthInside0LastX128, feeGrowthInside1LastX128, tokensOwed0,
                  and tokensOwed1.
        """
        return self.contract.functions.positions(i).call()

    def protocolFees(self) -> list:
        """Retrieves protocol fees for both token0 and token1.

        Returns
        -------
            list: A list containing token0 and token1 protocol fees.
        """
        return self.contract.functions.protocolFees().call()

    def slot0(self) -> list:
        """Retrieves slot0 data for the pool.

        Returns
        -------
            list: A list containing sqrtPriceX96, tick, observationIndex, observationCardinality,
                  observationCardinalityNext, feeProtocol, and unlocked status.
        """
        return self.contract.functions.slot0().call()

    def snapshotCumulativesInside(self, tickLower: int, tickUpper: int) -> list:
        """Retrieves snapshot cumulative data for the specified tick range.

        Args:
        ----
            tickLower (int): The lower tick of the range.
            tickUpper (int): The upper tick of the range.

        Returns:
        -------
            list: A list containing tickCumulativeInside, secondsPerLiquidityInsideX128, and secondsInside.
        """
        return self.contract.functions.snapshotCumulativesInside(
            tickLower,
            tickUpper,
        ).call()

    def tickBitmap(self, i: int) -> int:
        """Retrieves tick bitmap data for a specified index.

        Args:
        ----
            i (int): The index for which to retrieve tick bitmap data.

        Returns:
        -------
            int: The tick bitmap data for the specified index.
        """
        return self.contract.functions.tickBitmap(i).call()

    def tickSpacing(self) -> int:
        """Retrieves the tick spacing of the pool.

        Returns
        -------
            int: The tick spacing of the pool.
        """
        return self.contract.functions.tickSpacing().call()

    def ticks(self, i: int) -> list:
        """Retrieves tick-related data for a specified index.

        Args:
        ----
            i (int): The index for which to retrieve tick data.

        Returns:
        -------
            list: A list containing liquidityGross, liquidityNet, feeGrowthOutside0X128, feeGrowthOutside1X128,
                  tickCumulativeOutside, secondsPerLiquidityOutsideX128, secondsOutside, and initialized status.
        """
        return self.contract.functions.ticks(i).call()

    @lru_cache
    def token0(self) -> ERC20TokenContract:
        """Retrieves the ERC20 token contract instance for token0.

        Returns
        -------
            ERC20TokenContract: An instance of the ERC20TokenContract for token0.
        """
        return ERC20TokenContract(
            self.contract.functions.token0().call(),
            self.provider,
        )

    @lru_cache
    def token1(self) -> ERC20TokenContract:
        """Retrieves the ERC20 token contract instance for token1.

        Returns
        -------
            ERC20TokenContract: An instance of the ERC20TokenContract for token1.
        """
        return ERC20TokenContract(
            self.contract.functions.token1().call(),
            self.provider,
        )
