ticker = "READOR"
shares = 10
price = 333.30
value = shares * price

print ("Your own", shares, "shares of", ticker)
print ("Positon value", value)

tickers = ["READOR", "MSFT", "GOOGL"]
shares = [10, 5, 8]
prices = {
    "READOR": 333.30,
    "MSFT": 410.21,
    "GOOGL": 167.81
}

print (tickers)
print (tickers[0])
print (prices["READOR"])