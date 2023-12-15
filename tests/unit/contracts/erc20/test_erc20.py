from raffaelo.contracts.erc20.contract import ERC20TokenContract


def test__name__must_be_str(contract: ERC20TokenContract):  # noqa: D103
    assert isinstance(contract.name(), str)


def test__name__must_be_equal_to_usd_coin(contract: ERC20TokenContract):  # noqa: D103
    assert contract.name() == "USD Coin"


def test__total_supply__must_be_int(contract: ERC20TokenContract):  # noqa: D103
    assert isinstance(contract.totalSupply(), int)


def test__total_supply__must_be_more_than_zero(contract: ERC20TokenContract):  # noqa: D103
    assert contract.totalSupply() > 0


def test__decimals__must_be_int(contract: ERC20TokenContract):  # noqa: D103
    assert isinstance(contract.decimals(), int)


def test__decimals__must_be_more_than_zero(contract: ERC20TokenContract):  # noqa: D103
    assert contract.decimals() > 0


def test__balance_of__must_be_int(contract: ERC20TokenContract):  # noqa: D103
    assert isinstance(contract.balanceOf("0x8BD4B2312f6C95B0D40E7407b26b124B25cbA375"), int)


def test__balance_of__must_be_equal_to_zero(contract: ERC20TokenContract):  # noqa: D103
    assert contract.balanceOf("0x8BD4B2312f6C95B0D40E7407b26b124B25cbA375") == 0


def test__symbol__must_be_str(contract: ERC20TokenContract):  # noqa: D103
    assert isinstance(contract.symbol(), str)


def test__symbol__must_be_usdc(contract: ERC20TokenContract):  # noqa: D103
    assert contract.symbol() == "USDC"


def test__allowance__must_be_int(contract: ERC20TokenContract):  # noqa: D103
    assert isinstance(
        contract.allowance(
            "0x8BD4B2312f6C95B0D40E7407b26b124B25cbA375",
            "0x8BD4B2312f6C95B0D40E7407b26b124B25cbA375",
        ),
        int,
    )
