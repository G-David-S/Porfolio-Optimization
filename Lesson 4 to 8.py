# LESSONS CONINUE AFTER SLEEP
print("Lessons form 4 to 8 are here maybe even more")


# lesson 4 and 5
# for ---> is a keyword. It's followed by a condition: an expression that Python evaluates down to either True or False
# The full family is: >, <, >=, <=, == (equal to — two equals signs, because one = is assignment, which you already know),
# and != (not equal to).
# The colon : at the end means "a block follows" — the exact same rule as the colon after for ... in ...:.
# The indented line under if is the block that runs only if the condition is True.

# elif value > 10000: — short for "else if." Python only even checks this condition if the if above it was False.
# If this one's True, this block runs and everything else in the chain gets skipped.
# else: — the catch-all. No condition needed, nothing after it except the colon. It only runs if every if/elif above it was False

# Because if/elif/else are chained together like this, exactly one of the three blocks runs per loop pass — never zero, never more than one.

# def -----> keyword that means "I'm defining a function starting here." Short for "define." categorize_stock — the name you're giving this function.
# (value) — the parameter. This is a placeholder variable that only exists inside the function. When you call the function later and hand it a number,
# that number gets copied into value for the function to use. It's like a blank you fill in each time you use the function.
# : — same as with if and for: it means "the function's body starts on the next line, indented.

# return category — this is the new keyword. return sends a value back out of the function to wherever the function was called from.
# Without return, the function would run its logic but hand nothing back — result would end up empty. Think of return as the function's answer.


def categorize_stock(value):
    if value >= 15000:
        category = "LARGE"
    elif value >= 10000:
        category = "MEDIUM" 
    else:
        category = "SMALL"
    return category

portfolio = {
    "RDOR": 21000,
    "APPL": 13000,
    "TSLA": 8000,
}

for ticker, value in portfolio.items():
    result = categorize_stock(value)
    print(ticker, "is categorized as:", result)


import statistics

stock_prices = [1200, 3400, 5600]
avrage_price = statistics.mean(stock_prices)
print("Avrage stock price:", avrage_price)

#lesson 6 Imponrting 
# import ----> is a keyword — it tells Python "go load another file's worth of pre-written code so I can use it here."
# statistics -----> is the name of a module — a separate file full of functions someone already wrote (comes with python for free)
# This line has to come before you use anything from statistics later in the file. Python runs top to bottom, 
# so if this were below line 5, you'd get an error saying statistics doesn't exist yet.
# statistics.mean —----> the . reaches inside the module and pulls out one specific function from it.
# Read it right-to-left: "the mean function that lives inside statistics."
# (stock_prices) — same function-call syntax from Lesson 5. mean is a function, stock_prices is the single argument you're handing it.

#Lesson 7 Error handling - try / except

stock_data = { "AAPL": 150, "TSLA": 700}
ticker = "AAPL"
try:
    price = stock_data[ticker]
    print("Price", price)
except KeyError:
    print("No data found for", ticker)

# try: ----> A keyword, followed by : and an indented block — same shape as if
# It means "attempt to run this code, and if something goes wrong inside it, don't crash the whole program — hand control to EXCEPT (except) instead
# except ----> is the partner keyword to try — its block only runs if the try block hit a problem.
# KeyError ----> is the name of a specific kind of error — specifically, "you tried to look up a dictionary key that doesn't exist."
# If the code in try raises a KeyError, execution jumps straight into this block. If it raised some other kind of error, this except wouldn't catch it, and the program would still crash
# — this is why naming the specific error matters.
# Only one block runs — same rule as if/else. If try succeeds with no error, except never runs at all.

# This matters for your project because pulling live stock data from the internet will fail sometimes —
# a wrong ticker symbol, a dropped connection, a bad API response. Without try/except, one bad ticker would crash your entire program 
# instead of just reporting that one problem and moving on.



#Lesson 8 f-strings

stock = "AAPL"
price = 150.567
print(f"The price of {stock} is ${price}")
print(f"The price of {stock} is ${price:.2f}")

# The f right before the opening quote
# Marks this as an f-string (formatted string). It tells Python: "scan this string for {} and swap in real values"
# {stock} inside the string
# {} Curly braces hold an expression — here just a variable — and Python drops its value directly into the string at that exact spot.
# F-strings let you write the sentence exactly as you want it, with variables slotted in wherever you put {}.
# {price:.2f}
#  The colon starts a format spec — instructions for how to display the value, not just what value to show.
# .2f means "fixed-point notation, 2 digits after the decimal." Without it, price prints as the raw 150.567. With it, you get 150.57
# The $ inside the string  Just a literal character. Nothing special — it's not part of Python syntax, it's just text sitting next to the {}



# Test 0-8
Total_portfolio_value = 0
portfolio = {
    "AAPL": 187.32,
    "TSLA": 242.10,
    "GOOG": 138.75,
    "MSFT": 402.50
}

def categorize_stocks(price):
    if price >= 300:
        category = "LARGE"
    elif price >= 150:
        category = "MEDIUM"
    else:
        category = "SMALL"
    return category 


for ticker, price in portfolio.items():
    result = categorize_stocks(price)
    print(f"The price of {ticker}, is ${price:.2f}, - {result}")
    price_of_each = price 
    Total_portfolio_value = Total_portfolio_value + price_of_each


print(f"Total portfolios value {Total_portfolio_value:.2f}")

import statistics
portfolio_value_list = list(portfolio.values())
avrage_prices = statistics.mean(portfolio_value_list)
print(f"The avrage price of stocks is {avrage_prices:.2f}")

try:
    print(portfolio["NFLX"])
except KeyError:
    print("No data found for", "NFLX")  