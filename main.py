from binance import Client
from Functions import *


def total_usdt(pair_prices, balance):
    print("Account Balance: ")
    for y in usdt_crypto(total_balance(info), prices):
        for x in total_balance(info):
            if x['asset'] + "USDT" in y['symbol']:
                print("\t{}: {} $".format(x['asset'], float(y['price']) * float(x['free'])))
    return


client = Client("pVlXHvGbbrtltRFymi9cGdpI7q2M78oOuVEY6ZgQfR8TrWNcH8ZPshhlp910K7W9",
                "IEHMTQevnfVbMcvH4HmQXEM39BS2w791smodHXRxVHUB3OI2ouekhWdDl9D8O9y4")


info = client.get_account()
prices = client.get_all_tickers()

total_balance(info)
usdt_crypto(total_balance(info), prices)
total_usdt(usdt_crypto(total_balance(info), prices), total_balance(info))

