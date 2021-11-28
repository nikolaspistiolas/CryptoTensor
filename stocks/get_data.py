import yfinance as yf
import pandas as pd

# There are 2 tables on the Wikipedia page
# we want the first table

payload=pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
first_table = payload[0]
second_table = payload[1]

symbols = first_table['Symbol'].to_numpy()

for s in symbols:
    try:
        data = yf.download(s, start="2020-01-01",end="2021-10-10", group_by='tickers', interval='1h')
        data.to_csv(f'./data/{s}.csv')
        print(s)
    except Exception:
        print(s,'Exception')

