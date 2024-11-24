Here’s a concise and clear README file for your crypto trading project:

TrendTrader

An open-source crypto trading bot that utilizes the Alpaca Crypto Trading API to automate buying during market downturns and selling when a 2% profit target is reached.

Features

	•	Market Monitoring: Analyzes crypto price trends to identify buying opportunities during downturns.
	•	Automated Trading: Places buy and sell orders based on predefined strategies.
	•	Customizable Parameters: Easily adjust thresholds for buying and profit targets.
	•	Built on Alpaca API: Seamless integration with Alpaca’s crypto trading platform.

Getting Started

	1.	Clone the repository:

git clone https://github.com/dwisnowski/trade-wiz.git
cd TrendTrader


	2.	Install dependencies:

pip install -r requirements.txt


	3.	Set up Alpaca API keys:
	•	Sign up at Alpaca.
	•	Obtain your API key and secret, and add them to the code.
	4.	Run the bot:

python trend_trader.py



Configuration

	•	Edit the trading parameters in trend_trader.py:
	•	BUY_THRESHOLD: Percentage drop to trigger a buy (default: -1.5).
	•	SELL_PROFIT_PERCENT: Minimum profit percentage to sell (default: 2.0).

License

This project is licensed under the MIT License.

Disclaimer

This bot is for educational purposes only. Use it at your own risk. Crypto trading involves significant financial risk, and past performance is not indicative of future results.

