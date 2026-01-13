from binance import Client
from binance.exceptions import BinanceAPIException
from logger import logger


class BasicBot:
    def __init__(self, api_key, api_secret):
        # Binance Futures Testnet configuration
        self.client = Client(api_key, api_secret, testnet=True)
        self.client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

    def place_market_order(self, symbol, side, quantity):
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity
            )
            logger.info(f"Market order placed: {order}")
            return order
        except BinanceAPIException as e:
            logger.error(f"Market order failed: {e}")
            return None

    def place_limit_order(self, symbol, side, quantity, price):
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                timeInForce="GTC",
                quantity=quantity,
                price=price
            )
            logger.info(f"Limit order placed: {order}")
            return order
        except BinanceAPIException as e:
            logger.error(f"Limit order failed: {e}")
            return None

    # BONUS ORDER TYPE
    def place_stop_limit_order(self, symbol, side, quantity, stop_price, price):
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="STOP",
                quantity=quantity,
                stopPrice=stop_price,
                price=price,
                timeInForce="GTC"
            )
            logger.info(f"Stop-Limit order placed: {order}")
            return order
        except BinanceAPIException as e:
            logger.error(f"Stop-Limit order failed: {e}")
            return None
