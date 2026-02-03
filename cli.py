import argparse
import os
from dotenv import load_dotenv

from bot.client import BinanceFuturesClient
from bot.orders import place_order
from bot.logging_config import setup_logging

def main():
    load_dotenv()
    setup_logging()

    parser = argparse.ArgumentParser(
        description="Binance Futures Testnet Trading Bot"
    )
    parser.add_argument("--symbol", required=True, help="e.g. BTCUSDT")
    parser.add_argument("--side", required=True, choices=["BUY", "SELL"])
    parser.add_argument("--type", required=True, choices=["MARKET", "LIMIT"])
    parser.add_argument("--quantity", type=float, required=True)
    parser.add_argument("--price", type=float, help="Required for LIMIT orders")

    args = parser.parse_args()

    client = BinanceFuturesClient(
        api_key=os.getenv("BINANCE_API_KEY"),
        api_secret=os.getenv("BINANCE_API_SECRET"),
    )

    try:
        response = place_order(
            client=client,
            symbol=args.symbol,
            side=args.side,
            order_type=args.type,
            quantity=args.quantity,
            price=args.price,
        )

        print("\nOrder Summary")
        print("-" * 30)
        print(f"Order ID     : {response.get('orderId')}")
        print(f"Status       : {response.get('status')}")
        print(f"Executed Qty : {response.get('executedQty')}")
        print(f"Avg Price    : {response.get('avgPrice', 'N/A')}")
        print("\n✅ Order placed successfully")

    except Exception as e:
        print("\n❌ Order failed")
        print(str(e))

if __name__ == "__main__":
    main()
