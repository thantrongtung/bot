import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import binance
from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager
import pandas as pd
import numpy as np
import pandas
from datetime import datetime
import matplotlib.pyplot as matplt
import warnings
from replit import db
import time

warnings.filterwarnings('ignore')
api_key = "ycjUQfTfkOpC0ILTbBS4v1ZNxBHe74edVhb79snz2GmirGrtIsX1synAer8na1oh"
api_secret = "ellMgmentM7Z0AGKYTxLka74EwU1T8cux4tqkDXRO8NQNBYwTtxP1GsO8igGZPwN"
client = Client(api_key, api_secret)
asset1 = 'BTCUSDT'
asset2 = 'BTCBUSD'
print(len(db['price']))
while True:
  data1 = float(client.futures_orderbook_ticker(symbol=asset1)['bidPrice'])
  data2 = float(client.futures_orderbook_ticker(symbol=asset2)['bidPrice'])
  db['price'].append([data1,data2])
  #print(data1,data2)