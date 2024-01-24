import json
import os
import time
import threading
from pprint import pprint
from random import random
import websocket
from binance.client import Client
from binance.websockets import BinanceSocketManager

api_key = 'ad08cd0dca0ad5465e9b309259df0216931329d71422116937576e943c4352c0'
api_secret = 'b233aedcb230204d811f21efecf8714d5af13b8a992f00d024270c75f871132d'

SOCKET = 'wss://stream.binance.com:9443/ws/ethusdt@kline_1m'

client = Client(api_key, api_secret)
bm = BinanceSocketManager(client)
rsiA = 14
rsiB = 1
wtA = 10
wtB=11
ccA = 20
ccB = 1
adxA = 20
adxB=2
rsi1A = 9
rsi1B = 1
maxBarsBack=2000
source="close"
neighborsCount=8
signal="long"
signalSell="short"
useVolatilityFilter= True
useRegimeFilterThreshold=-0.1
useAdxFilterThreshold=20
UseEmaFilterPeriod=50
useSmallEmaFilterPeriod=50
def handle_message(msg):
    candle=msg['k']
    close= candle['c']
    is_candle_closed = candle['x']
    print(is_candle_closed)
    if is_candle_closed:
        print("candle closed at {}".format(close))

# Start Kline Socket
conn_key = bm.start_kline_socket('ETHUSDT', handle_message)
bm.start()

# You can run your own logic here, or just keep the program alive
# For example, you might want to use a loop with time.sleep to keep the program running
while True:
    time.sleep(1)
