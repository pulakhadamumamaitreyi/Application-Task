import logging
from binance.client import Client
from binance.exceptions import BinanceAPIException, BinanceRequestException

logger = logging.getLogger(__name__)

TESTNET_BASE_URL = "https://testnet.binancefuture.com"

class BinanceFuturesClient:
    def __init__(self, api_key: str, api_secret: str):
        self.client = Client(api_key, api_secret)
        self.client.FUTURES_URL = TESTNET_BASE_URL

    def create_order(self, **params):
        try:
            logger.info(f"Placing order: {params}")
            response = self.client.futures_create_order(**params)
            logger.info(f"Order response: {response}")
            return response
        except (BinanceAPIException, BinanceRequestException) as e:
            logger.exception("Binance API error")
            raise
        except Exception as e:
            logger.exception("Unexpected error")
            raise
