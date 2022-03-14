import requests
from selenium import webdriver
import os
import time
import wget

save_dir = './'
with open('./zips/symbols.txt', 'r') as f:
    symbolsi = f.readlines()
print('ok')
symbols = []
for i in symbolsi:
    symbols.append(i.rstrip())


driver = webdriver.Chrome(os.getcwd()+'/chromedriver')

for s in symbols:
    driver.get(f"https://data.binance.vision/?prefix=data/spot/monthly/klines/{s}USDT/1h/")
    time.sleep(5)
    elems = driver.find_elements_by_xpath("//a[@href]")
    for elem in elems:
        hrefi = elem.get_attribute("href")
        if 'zip' in hrefi and 'CHECK' not in hrefi:
            print(hrefi)
            res = wget.download(hrefi)
            # filename = hrefi.split('/')[-1]
            # open(save_dir + filename, 'w').write(res.content)
