# Stock Portfolio Tracker
portfolio = {
    "AAPL": 10,
    "GOOG": 5,
    "TSLA": 2
}

prices = {
    "AAPL": 150.0,
    "GOOG": 2800.0,
    "TSLA": 700.0
}

total_value = 0
for stock, shares in portfolio.items():
    stock_value = shares * prices.get(stock, 0)
    total_value += stock_value
    print(f"{stock}: {shares} shares × ${prices[stock]} = ${stock_value}")

print(f"Total Portfolio Value: ${total_value}")
