from bot.validators import (
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price,
)

def place_order(
    client,
    symbol: str,
    side: str,
    order_type: str,
    quantity: float,
    price: float | None = None,
):
    validate_side(side)
    validate_order_type(order_type)
    validate_quantity(quantity)
    validate_price(price, order_type)

    params = {
        "symbol": symbol.upper(),
        "side": side,
        "type": order_type,
        "quantity": quantity,
    }

    if order_type == "LIMIT":
        params["price"] = price
        params["timeInForce"] = "GTC"

    return client.create_order(**params)
