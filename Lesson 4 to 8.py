# LESSONS CONINUE AFTER SLEEP
print("Lessons form 4 to 8 are here maybe even more")



# for ---> is a keyword. It's followed by a condition: an expression that Python evaluates down to either True or False
# The full family is: >, <, >=, <=, == (equal to — two equals signs, because one = is assignment, which you already know),
# and != (not equal to).
# The colon : at the end means "a block follows" — the exact same rule as the colon after for ... in ...:.
# The indented line under if is the block that runs only if the condition is True.

# elif value > 10000: — short for "else if." Python only even checks this condition if the if above it was False.
# If this one's True, this block runs and everything else in the chain gets skipped.
# else: — the catch-all. No condition needed, nothing after it except the colon. It only runs if every if/elif above it was False

# Because if/elif/else are chained together like this, exactly one of the three blocks runs per loop pass — never zero, never more than one.

# def ---> keyword that means "I'm defining a function starting here." Short for "define." categorize_stock — the name you're giving this function.
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
