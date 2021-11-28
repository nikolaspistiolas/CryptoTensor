import pymongo

cl = pymongo.MongoClient('mongodb://%s:%s@178.128.23.182' % ('nikolaspistiolas','nikolaspistiolas'))
db = cl['production']
col = db['symbols']

symbols = [i['symbol'] for i in col.find()]

ret = 100
state = {
    'balance' : 100,
    'open_up':False,
    'open_down':False,
    'open': 0
}
for j in range(1,10):
    j /= 10
    n = 0
    ret = 100
    for s in symbols:
        data = [ i for i in db['signal'].find({'symbol':s}).sort('date',pymongo.ASCENDING)]
        for i in range(len(data)-1):
            # if data[i]['neural_up'] > 0.4:
            #     ret *= 1 + (data[i + 1]['last_price'] - data[i]['last_price']) / data[i]['last_price'] - 0.002
            # elif  data[i]['neural_down'] > 0.4:
            #     ret *= 1 - (data[i + 1]['last_price'] - data[i]['last_price']) / data[i]['last_price'] - 0.002
            if data[i]['neural_output'] > j:
                ret *= 1 + (data[i+1]['last_price']-data[i]['last_price'])/data[i]['last_price'] #- 0.002
                n += 1
            if data[i]['neural_output'] < -j:
                ret *= 1 - (data[i+1]['last_price']-data[i]['last_price'])/data[i]['last_price'] #- 0.002
                n += 1


    print(ret,j,n)