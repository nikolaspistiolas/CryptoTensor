from binance.client import Client
from binance.helpers import round_step_size

client = Client('Hyfql9duSigJUWT4vAJJO7fOAz2TFOHpuYvk7aXjLAkRjm5eK0vbIWsumZvvzp2G',
                'm60s3JnaNEnbH1XLQESPhB6UHxIhdwuibh6uT9mSw1lqCP0ygQebUkOnt31AXsj5')


def opening_hour():
    # code to run at the begining of the hour
    pass


def closing_hour():
    # code to run at the end of the hour
    pass


def open_buy_order(symbol,amount):
    pass

def close_market_order(symbol):
    pass

def open_sell_order(symbol,amount):
    pass

def close_sell_order(symbol,amount):
    pass

print(client.get_account_status())



info = client.get_symbol_info('ZECUSDT')

# print(client.get_asset_balance(asset='USDT'))
# zec = client.get_asset_balance(asset='ZEC')['free']
# print(zec)
# tick_size = 0.00001
# rounded_amount = round_step_size(float(zec), tick_size)
# client.order_market_sell(symbol = 'ZECUSDT',quantity=rounded_amount)
# print(client.get_asset_balance(asset='USDT'))
# print(client.get_asset_balance(asset='ZEC'))


# print(info)
# for i in info['balances']:
#     if float(i['free']) != 0 or float(i['locked'])!=0:
#         print(i)
#
# print(client.get_deposit_history())

