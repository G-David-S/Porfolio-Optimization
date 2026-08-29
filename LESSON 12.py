# LESSON 12

import yfinance as yf
import concurrent.futures
import time

tickers = ["AAPL", "MSFT", "TSLA", "JNJ", "XOM"]

def get_price(symbol):
    stock = yf.Ticker(symbol)
    info = stock.fast_info
    return f"{symbol}: ${info['lastPrice']}"

start = time.time()

with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    results = executor.map(get_price, tickers)

for line in results:
    print(line)

end = time.time()
print(f"Took {end - start:.2f} seconds")