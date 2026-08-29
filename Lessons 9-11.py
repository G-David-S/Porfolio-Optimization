#here are lessons 9 thorugh 12
#LESSON 9

# [ ] —---> the outer square brackets tell Python "build a list from this."

# Breaking down every piece of [ticker for ticker, price in stock_prices.items() if price > 200]
# ticker (the very first thing inside the brackets) — this is the expression. It's what actually gets put into the new list on each pass.
# if price > 200 — a filter. For each pair, Python only evaluates the expression and adds it to the list when this is True. Leave it off and every item gets included.
# Notice there's no .append() anywhere. That's the entire point of this syntax — it does the "create empty list, loop, append" pattern for you in one expression

stock_prices = {"AAPL": 189.50, "MSFT": 230.21, "TSLA": 150.31, "GOOGL": 302.10}
expensive_stocks = [ticker for ticker, price in stock_prices.items() if price > 200] 
rounded_prices = [round(price) for ticker, price in stock_prices.items() if price > 200]
print("The expensive stocks and their matching prices are:", expensive_stocks, rounded_prices)

# LESSON 10 ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Right now, if you wanted to represent a stock, you'd probably use a dictionary: {"ticker": "AAPL", "price": 150.25, "shares": 10}. That works, 
# but it doesn't scale — nothing stops you from misspelling a key, and there's no clean way to attach behavior (like "calculate this stock's value") 
# to the data itself. A class fixes both problems: it bundles data and the functions that act on that data into one reusable blueprint.

# class Stock: —----> class is the keyword that starts a blueprint definition. Stock is the name we're giving it. Notice the capitalization style:
#  Stock, not stock — this is a Python convention (called PascalCase) that signals "this is a class," the same way you'd use lowercase for a normal variable



class Stock:
    def __init__(self, ticker, price, shares):
        self.ticker = ticker
        self.price = price
        self.shares = shares
      

    def total_value(self):
        return self.price * self.shares
    
    def is_profitable(self, purchuse_price):
        return self.price > purchuse_price

aapl = Stock("AAPL", 150.50, 10)
msft = Stock("MSFT", 310.21, 6)
redr = Stock("REDR", 185.1 ,10)
anime = Stock("ANIME", 82, 18)

portfolio = [aapl, msft, redr, anime]

for stock in portfolio:
    value = stock.total_value()
    print(f"{stock.ticker}: {stock.shares} shares at ${stock.price:.2f} = ${value:.2f}")
    if stock.is_profitable(152):
        print(f"{stock.ticker} is profitable if sold at this moment")
    else:
        print(f"{stock.ticker} is not profitable if sold at this moment")

# def __init__(self, ticker, price, shares): — this defines a special method. __init__ is not a name you chose — it's a fixed name Python looks for 
# automatically. The double underscores on each side are called "dunder" (short for double underscore), and they mark this as one of Python's built-in special
# method names. Whenever you create a new Stock, Python runs this method for you automatically, right at the moment of creation. 
# This is why it's called a constructor — it constructs the object.

# self refers to "this specific object being built or acted on." It's always the first parameter in any method inside a class,
# Think of it as Python silently saying "here's the object we're working on" every time a method runs.
# ticker, price, shares — ordinary parameters,

# self.ticker = ticker — the dot (.) is new syntax: it means "access or assign something that belongs to an object."
# The left side, self.ticker, creates a piece of data called ticker and stores it on this object.
# def total_value(self): — a normal method, but it only needs self as a parameter — no other input — 
# because everything it needs (self.price, self.shares) is already stored on the object.

# aapl = Stock("AAPL", 150.25, 10) — this is called instantiating the class: creating an actual object from the blueprint. 
# It looks like a function call, but calling a class name like this triggers __init__ behind the scenes. The three values map onto ticker, price, shares 
# — self is skipped because Python supplies it automatically (it's the new object itself, aapl).

# msft = Stock(...) — a second, completely independent object. aapl and msft each hold their own separate ticker/price/shares —
# No need to pass self manually here either — Python knows "self" is stock because that's what you called the method on



# LESSON 12 imported YFINANCE
# import yfinance as yf — as creates an alias. yfinance is the module's real name, but typing it out every time is annoying, 
# so as yf lets you refer to it as yf for the rest of the file.

import yfinance as yf

tickers = ["AAPL", "MSFT", "TSLA"]

for symbol in tickers:
    stock = yf.Ticker(symbol)
    info = stock.info
    print(f"{symbol}: {info['longName']} - ${info['currentPrice']}")