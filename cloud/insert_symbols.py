import pymongo



cl = pymongo.MongoClient('mongodb://%s:%s@178.128.23.182' % ('nikolaspistiolas','nikolaspistiolas'))
db = cl['production']
col = db['symbols']

symbols = ['btcusdt','ethusdt','eosusdt','bchusdt','neousdt','etcusdt','bnbusdt','qntusdt','zecusdt','dashusdt','manausdt']

for i in symbols:
    col.insert_one({'active':True, 'symbol':i.upper()})