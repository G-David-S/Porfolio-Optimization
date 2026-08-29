# LESSON 12

import yfinance as yf
import time

tickers = [
    "AAPL", "MSFT", "NVDA", "AMZN", "GOOGL", "GOOG", "META", "AVGO", "TSLA", "BRK-B",
    "LLY", "WMT", "JPM", "V", "ORCL", "XOM", "MA", "JNJ", "COST", "NFLX",
    "MU", "PLTR", "HD", "ABBV", "BAC", "PG", "GE", "KO", "CRM", "CVX",
    "AMD", "CSCO", "IBM", "WFC", "PM", "MS", "GS", "CAT", "ABT", "LIN",
    "RTX", "MCD", "AXP", "TMO", "INTU", "ISRG", "AMAT", "PEP", "DIS", "UBER",
    "QCOM", "TXN", "NEE", "VZ", "NOW", "BKNG", "SPGI", "ADBE", "HON", "PFE",
    "BLK", "TJX", "LOW", "SYK", "C", "ANET", "GILD", "DE", "LRCX", "BSX",
    "VRTX", "MDT", "SCHW", "ADP", "MMC", "AMGN", "PGR", "CI", "CB", "SO",
    "PANW", "ADI", "COP", "REGN", "MO", "BMY", "DUK", "KLAC", "CME", "ICE",
    "INTC", "SNPS", "CDNS", "ETN", "CRWD", "FI", "PLD", "UPS", "WM", "NKE",
    "ELV", "SHW", "MDLZ", "MCO", "EQIX", "APH", "GD", "HCA", "TT", "EOG",
    "ITW", "USB", "PNC", "EMR", "MAR", "CL", "ORLY", "AJG", "CTAS", "MPC",
    "APD", "MMM", "MSI", "TDG", "AON", "FDX", "NSC", "ECL", "WELL", "PSA",
    "FTNT", "SRE", "COF", "AEP", "TGT", "WMB", "ROP", "DHR", "AZO", "KMI",
    "BK", "JCI", "MET", "TRV", "AFL", "O", "DLR", "CARR", "TEL", "PAYX",
    "SPG", "CMCSA", "STZ", "MNST", "ADSK", "ROST", "ALL", "FAST", "GWW", "FIS",
    "URI", "PCAR", "PSX", "VLO", "OXY", "AIG", "AMP", "EXC", "KDP", "EA",
    "FISV", "CTVA", "KR", "D", "EW", "IDXX", "OTIS", "YUM", "AME", "LHX",
    "CMG", "LULU", "IQV", "GEHC", "PAYC", "RSG", "ODFL", "HUM", "WBD", "NOC"
]

start = time.time()

data = yf.download(
    tickers,
    period="1d",
    interval="1m",
    group_by="ticker",
    auto_adjust=False,
    progress=False,
    threads=True
)

for ticker in tickers:
    try:
        prices = data[ticker]["Close"].dropna()

        if len(prices) > 0:
            price = prices.iloc[-1]
            print(f"{ticker}: ${price:.2f}")
        else:
            print(f"{ticker}: NO DATA")

    except Exception as e:
        print(f"{ticker}: ERROR - {e}")

end = time.time()

print(f"\nTook {end - start:.2f} seconds")