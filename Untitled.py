ticker = "READOR"
shares = 10
price = 333.30
value = shares * price

print ("Your own", shares, "shares of", ticker)
print ("Positon value", value)

tickers = ["READOR", "MSFT", "GOOGL"]
prices = {
    "READOR": 333.30,
    "MSFT": 410.21,
    "GOOGL": 167.81
}

shares = {
    "READOR": 10,
    "MSFT": 5,
    "GOOGL": 8
}

total_value = 0


print (tickers)
print (tickers[0])
print (prices["READOR"])

#lessons so far: when in a dictionary all things are numbered fomr 0
# make sure to put , to seperate things
# =  ---> means that a veriable means THIS
# when displaying text always put it in ""
# [] ----> means list, all things in it are numbered
# {} ---> means dictionary (szótár) so in these insted of numberd positons each things in it has a VALUE PAIR with a KEY
# for example if my KEY is "APPLE" and my value is "100" then it woud be prices = {APPLE: 100} so if i print this its 100

for ticker in tickers:
    print(ticker)

# for —--> a keyword that starts the loop. It tells Python "repeat what follows, once per item
# in —--> pairs the loop variable with the collection you're looping over. Reads naturally: "for ticker in tickers
# : —--> the colon marks "everything indented below this line is what happens on each pass.

for ticker, price in prices.items():
    print(ticker, "is trading at", price)

# .items() —--> a method that exists on every dictionary. It hands you back each key and value together, as a pair, 
# instead of just the keys. Without .items(), a loop over a dict only gives you the keys, one at a time 
# — you'd have no way to get the price in the same line

# ticker, price — since .items() gives you a pair each time, Python lets you unpack that pair into two variable names in one go
# , separated by a comma.ticker catches the first half of the pair (the key), price catches the second half (the value).
# . You choose both names — Python doesn't care what you call them, but the order matters:
# KEY first, VALUE second

for ticker, price in prices.items():
    value = price * shares[ticker]
    total_value = total_value + value
    print(ticker, "positon value", value)

print("Total portfolio value:", total_value)

# total_value = 0 —--> set up before the loop starts. This is a running total that the loop will update on each pass.
# It has to exist before the loop, or there'd be nothing to add to
# shares[ticker] —---> you already know how to pull a value out of a dict using a literal key, like shares["AAPL"].
# This is the same thing, except the key is a variable (ticker) instead of a fixed string.
# Since ticker changes value on each pass of the loop, shares[ticker] looks up a different share count each time

# total_value = total_value + value —--> 
# the right side (total_value + value) is calculated first, using whatever total_value currently holds, 
# and only then does the result get stored back into total_value.
# So each pass through the loop, this line means "take the running total, add this position's value, and that becomes the new running total."
# By the end of the loop, total_value holds the sum of everything.