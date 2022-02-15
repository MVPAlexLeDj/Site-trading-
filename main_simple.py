import sys
import os, sys
from botorderclient import BotOrderClient
import time

sys.path.append(os.path.join(os.path.dirname(__file__), 'Site-Trading-'))

from robotrading import RoboTrading

client = BotOrderClient()
gains = []
timestamp = []
robot = RoboTrading(client)

with open("candle_sample.txt", "r") as fp:
    lines = fp.readlines()
    for line in lines:
        client.process_candle(line)
        robot.process_candle(line)
        gains += [ client.gains() ]
        timestamp += [client.last_time]

print(f"Gains : {client.gains()}")
