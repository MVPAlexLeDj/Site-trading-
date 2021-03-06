import json
class RoboTrading():

    def __init__(self, client):
        """
        client is used to issue orders
        """
        self.client = client
        self.previous_price = 0

    def process_candle(self, candle_msg:str):
        """This function is called when a new candle_msg is received.
            Candle message is a string of the form:
            {'symbol_key' : {'c': [174.3], 'h': [174.3], 'l': [174.19], 'o': [174.19], 's': 'ok', 't': [1643670000], 'v': [1888]}

            Note that there are list, so you can have multiple candles in one message.
        """
        parsed = json.loads(candle_msg)
        if 'AAPL' in parsed:
            if self.client.money > parsed['AAPL']['c']:
                if self.previous_price > parsed['AAPL']['c']:
                    self.client.buy('AAPL', 1)
            if self.client.actions['AAPL'] > 1:
                if self.previous_price < parsed['AAPL']['c']:
                    self.client.sell('AAPL', 1)

            self.previous_price = parsed['AAPL']['h']