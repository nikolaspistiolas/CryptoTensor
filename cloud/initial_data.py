import requests
import pymongo
from datetime import datetime

base_url = 'https://api3.binance.com'

cl = pymongo.MongoClient('mongodb://%s:%s@159.223.48.44' % ('nikolaspistiolas','nikolaspistiolas'))
print(cl.list_databases())
db = cl['production']
col = db['data']
symbols = db['symbols'].find({'active':True})

interval = '1h'

def insert_data(symbol, col):
    interval = '1h'
    res = requests.get(base_url+f'/api/v3/klines?symbol={symbol}&interval={interval}').json()
    res = res[:-1]
    for i in res:
        up = {}
        up['symbol'] = symbol
        up['time'] = datetime.fromtimestamp(i[0]/1000)
        up['open'] = i[1]
        up['high'] = i[2]
        up['low'] = i[3]
        up['close'] = i[4]
        up['volume'] = i[7]
        col.insert_one(up)
    print(up)
    return

for i in symbols:
    insert_data(i['symbol'], col)
