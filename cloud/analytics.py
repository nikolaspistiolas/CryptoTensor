import ta
import pymongo
from tensorflow.keras.models import load_model, Model
from tensorflow import keras
from tensorflow.keras.layers import Flatten, Dense, Dropout, Activation, Input, Reshape, Conv2D, MaxPooling2D
import pandas as pd
from datetime import datetime

cl = pymongo.MongoClient('mongodb://%s:%s@159.223.48.44' % ('nikolaspistiolas','nikolaspistiolas'))
db = cl['production']
signals = db['signal']
symbols =[i['symbol'] for i in db['symbols'].find({'active':True})]

def simple_nn():
    input_lmd = Input(shape=(84))
    out = Dense(60, activation='relu')(input_lmd)
    out = Dense(30, activation='relu')(out)
    out = Dropout(0.2)(out)
    out = Dense(1, activation='linear')(out)
    model = Model(inputs=input_lmd, outputs=out)
    adam = keras.optimizers.Adam(lr=0.001, beta_1=0.9, beta_2=0.999, epsilon=1)
    model.compile(optimizer=adam, loss='mae')#, metrics=['mean_absolute_percentage_error','cosine_similarity'])
    model.summary()
    return model

def normalize(data, days=20):
    ret = pd.DataFrame()
    dont_norm = ['trend_psar_down_indicator', 'trend_psar_up_indicator', 'volatility_kchi', 'volatility_bbli',
                 'volatility_bbhi', 'volatility_kcli']
    for i in data.columns:
        if i not in dont_norm:
            ret[i] = (data[i] - data[i].rolling(days * 24).mean()) / data[i].rolling(days * 24).std()
        else:
            ret[i] = data[i]
    return ret


for i in symbols:
    data = db['data'].find({'symbol': i}).sort('time', pymongo.ASCENDING)
    data = pd.DataFrame.from_records(data)
    data["open"] = pd.to_numeric(data["open"], downcast="float")
    data["close"] = pd.to_numeric(data["close"], downcast="float")
    data["low"] = pd.to_numeric(data["low"], downcast="float")
    data["high"] = pd.to_numeric(data["high"], downcast="float")
    data["volume"] = pd.to_numeric(data["volume"], downcast="float")
    data = ta.add_all_ta_features(
        data, open="open", high="high", low="low", close="close", volume="volume", fillna=True)
    data = normalize(data[data.columns[3:-4]],days=15)
    data = data.to_numpy()
    data = data[-200:]

    model = load_model('./model.h5')
    res = model.predict(data)
    up = {'symbol':i,
          'date':datetime.now(),
          'neural_output': res[-1][0]}
    print(up)
    #break
    #signals.insert_one(up)