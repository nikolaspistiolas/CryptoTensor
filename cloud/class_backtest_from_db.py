import pymongo

cl = pymongo.MongoClient('mongodb://%s:%s@178.128.23.182' % ('nikolaspistiolas','nikolaspistiolas'))
db = cl['production']
col = db['symbols']

symbols = [i['symbol'] for i in col.find()]


state = {
    'balance': 100,
    'open_up': False,
    'open_down': False,
    'open': 0
}
for pollapl in range(170, 186, 5):
    pollapl /= 100
    c = 0
    ret = 100
    for s in symbols:
        if s != 'ZECUSDT' and s != 'DASHUSDT' :
            data = [i for i in db['signal_class'].find({'symbol': s}).sort('date', pymongo.ASCENDING)]

            for i in range(len(data)-1):
                if data[i]['neural_up'] > pollapl * data[i]['neural_stable'] and data[i]['neural_up'] > pollapl * data[i]['neural_stable']:
                    print(data[i]['symbol'],data[i]['date'])
                    c += 1
                    ret *= 1 + (data[i+1]['last_price']-data[i]['last_price'])/data[i]['last_price'] - 0.002
                elif data[i]['neural_down'] > pollapl * data[i]['neural_up'] and data[i]['neural_down'] > pollapl * data[i]['neural_stable']:
                    print('DOWN',data[i]['symbol'], data[i]['date'])
                    c += 1
                    ret *= 1 - (data[i+1]['last_price']-data[i]['last_price'])/data[i]['last_price'] - 0.002
    print(ret, pollapl, c)
