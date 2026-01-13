from basic_bot import BasicBot
from config import API_KEY, API_SECRET


# ---------- UI (CLI Enhancement) ----------
def display_menu():
    print("\n==============================")
    print(" Binance Futures Trading Bot ")
    print("==============================")
    print("1. Market Order")
    print("2. Limit Order")
    print("3. Stop-Limit Order")
    print("4. Exit")

    choice = input("Select an option (1-4): ").strip()

    menu_map = {
        "1": "MARKET",
        "2": "LIMIT",
        "3": "STOP",
        "4": "EXIT"
    }

    if choice not in menu_map:
        raise ValueError("Invalid menu selection")

    return menu_map[choice]


# ---------- Validation ----------
def validate_side(side):
    if side not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL")


def validate_quantity(qty):
    if qty <= 0:
        raise ValueError("Quantity must be greater than 0")


# ---------- Main ----------
def main():
    if not API_KEY or not API_SECRET:
        print("API keys are missing. Check your .env file.")
        return

    bot = BasicBot(API_KEY, API_SECRET)

    try:
        while True:
            order_type = display_menu()

            if order_type == "EXIT":
                print("Exiting application.")
                break

            symbol = input("Enter symbol (e.g. BTCUSDT): ").upper()
            side = input("Enter side (BUY or SELL): ").upper()
            quantity = float(input("Enter quantity: "))

            validate_side(side)
            validate_quantity(quantity)

            if order_type == "MARKET":
                result = bot.place_market_order(symbol, side, quantity)

            elif order_type == "LIMIT":
                price = float(input("Enter limit price: "))
                result = bot.place_limit_order(symbol, side, quantity, price)

            elif order_type == "STOP":
                stop_price = float(input("Enter stop price: "))
                price = float(input("Enter limit price: "))
                result = bot.place_stop_limit_order(
                    symbol, side, quantity, stop_price, price
                )

            if result:
                print("\n✅ Order processed successfully")
                print(result)
            else:
                print("\n❌ Order failed. Check logs/bot.log")

    except ValueError as ve:
        print(f"\nInput error: {ve}")

    except Exception as e:
        print(f"\nUnexpected error: {e}")


if __name__ == "__main__":
    main()
