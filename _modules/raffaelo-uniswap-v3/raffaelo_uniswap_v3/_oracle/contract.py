from functools import lru_cache

from raffaelo_uniswap_v3.pool.contract import UniSwapV3PoolContract


class UniSwapV3OracleContract(UniSwapV3PoolContract):

    @lru_cache
    def decimals(self) -> int:
        return self.token1().decimals() - self.token0().decimals()

    def sqrt_price_x96(self) -> int:
        return self.slot0()[0]
