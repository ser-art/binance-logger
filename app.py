import asyncio
import json
from datetime import datetime

import websockets

import numpy as np
from src.logger import get_logger
from src.settings import get_streams_string, get_sma_interval

sma_logger = get_logger(__name__)

db = {}


async def app():
    streams_string = get_streams_string()
    async with websockets.connect(streams_string) as websocket:
        async for message_str in websocket:
            message = json.loads(message_str)
            message = message['data']

            if not message['k']['x']:
                continue

            symbol = message['s']

            start_time = message['k']['t']
            start_time = datetime.fromtimestamp(int(start_time)/1000)
            start_time = str(start_time)

            close_time = message['k']['T']
            close_time = datetime.fromtimestamp(int(close_time)/1000)
            close_time = str(close_time)

            last_close_price = float(message['k']['c'])

            if not db.get(symbol):
                db[symbol] = {}
                db[symbol]['time_intervals'] = []
                db[symbol]['close_prices'] = []

            db[symbol]['close_prices'].append(last_close_price)

            n = get_sma_interval()
            sma_n = np.mean(db[symbol]['close_prices'][-n:])

            sma_logger.info(f"SMA({n}) for pair {symbol} and time interval {f'{start_time}-{close_time}'}: {sma_n}")


asyncio.run(app())
