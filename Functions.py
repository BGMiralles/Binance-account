def total_balance(account):
    """
    create the `balance` list with the amount of each cryptocurrency
    :param account: `client.get_account()`
    :return: returns the list with the amount of each cryptocurrency
    """
    balance = []
    for x in account['balances']:
        if float(x['free']) > 0:
            balance.append(x.copy())
    return balance


def usdt_crypto(balance, prices):
    """
    creates a list of the cryptocurrencies that are in `balance` with their prices in USDT
    :param balance: `total_balance(info)`
    :param prices: `client.get_all_tickers()`
    :return: returns a list of cryptocurrencies in `balance` with their price in USDT
    """
    pair_prices = []
    for x in balance:
        for y in prices:
            if x['asset'] + "USDT" in y['symbol']:
                pair_prices.append(y.copy())
    return pair_prices
