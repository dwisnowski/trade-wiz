import schedule

def run_trading_bot():
    trade_crypto("BTCUSD", 0.001)  # Replace with your desired crypto and quantity

schedule.every(1).minute.do(run_trading_bot)

while True:
    schedule.run_pending()
    time.sleep(1)