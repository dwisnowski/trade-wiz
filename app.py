import alpaca_trade_api as tradeapi
import time
import pandas as pd
import numpy as np

# Alpaca API credentials
API_KEY = "your_api_key"
SECRET_KEY = "your_secret_key"
BASE_URL = "https://paper-api.alpaca.markets"  # Use paper trading for testing

# Initialize Alpaca API
api = tradeapi.REST(API_KEY, SECRET_KEY, BASE_URL)


# Parameters
BUY_THRESHOLD = -1.5  # Percentage drop to trigger a buy
SELL_PROFIT_PERCENT = 2.0  # Minimum profit to sell

def get_crypto_price(symbol):
    """Fetch the latest price for a given cryptocurrency."""
    barset = api.get_crypto_bars(symbol, timeframe="1Min").df
    if not barset.empty:
        return barset["close"][-1]
    return None

def calculate_percent_change(prices):
    """Calculate percentage change between two prices."""
    return ((prices[-1] - prices[0]) / prices[0]) * 100

def check_buy_signal(symbol):
    """Check if the market is trending downward."""
    barset = api.get_crypto_bars(symbol, timeframe="5Min").df
    if not barset.empty:
        percent_change = calculate_percent_change(barset["close"].values[-5:])
        return percent_change <= BUY_THRESHOLD
    return False

def trade_crypto(symbol, quantity):
    """Execute buy or sell orders based on signals."""
    portfolio = api.get_account()
    positions = api.list_positions()
    
    # Check if we already hold this crypto
    current_position = next((p for p in positions if p.symbol == symbol), None)

    # Buy logic
    if current_position is None:
        if check_buy_signal(symbol):
            price = get_crypto_price(symbol)
            if price:
                api.submit_order(
                    symbol=symbol,
                    qty=quantity,
                    side="buy",
                    type="market",
                    time_in_force="gtc"
                )
                print(f"Bought {quantity} {symbol} at {price}")
    
    # Sell logic
    elif current_position:
        avg_price = float(current_position.avg_entry_price)
        current_price = get_crypto_price(symbol)
        if current_price and ((current_price - avg_price) / avg_price) * 100 >= SELL_PROFIT_PERCENT:
            api.submit_order(
                symbol=symbol,
                qty=quantity,
                side="sell",
                type="market",
                time_in_force="gtc"
            )
            print(f"Sold {quantity} {symbol} at {current_price} for profit")