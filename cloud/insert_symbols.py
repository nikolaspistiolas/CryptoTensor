import pymongo



cl = pymongo.MongoClient('mongodb://%s:%s@178.128.23.182' % ('nikolaspistiolas','nikolaspistiolas'))
db = cl['production']
col = db['symbols']

col.delete_many({})
with open('../zips/symbols.txt', 'r') as f:
    symbolsi = f.readlines()
print('ok')
symbols = []
for i in symbolsi:
    symbols.append(i.rstrip())

print(symbols)
input()

for i in symbols:
    col.insert_one({'active':True, 'symbol':i.upper() + 'USDT'})