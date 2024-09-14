#calculating with dictionaries

prices = {
       'ACME': 45.23,
       'AAPL': 612.78,
       'IBM': 205.55,
       'HPQ': 37.20,
       'FB': 10.75
}

sorted_prices = sorted(zip(prices.values(), prices.keys()))

print( f"Min: { sorted_prices[0]}")
print( f"Max: { sorted_prices[-1]}")

a = {
    'x' : 1,
    'y' : 2,
    'z' : 3 
}

b = {
    'w' : 10,
    'x' : 11,
    'y' : 2
}

c = {**a, **b}
print(f"c: {c}")
d = { key: c[key] for key in c.keys() - {'z', 'w'}}
print(f"d: {d}")

# create a dict of indian equities in BSE with share prices, p/e ratio, debt equity ratio
indian_equities = {
    'TCS': {'share_price': 1000, 'pe_ratio': 20, 'debt_equity_ratio': 0.5},
    'WIPRO': {'share_price': 500, 'pe_ratio': 15, 'debt_equity_ratio': 0.3},
    'INFY': {'share_price': 1500, 'pe_ratio': 25, 'debt_equity_ratio': 0.4}
}

def genFibonacci(n):
    a,b = 0,1

    # using generator expression 
    gen = (a+b for i in range(n))

    for i in range(n):
        print(next(gen))
        a,b = b,a+b

genFibonacci(20)
#a few test cases for genFibonacci(n)
print("Test cases for genFibonacci(n):")
genFibonacci(5)
genFibonacci(10)


def my_generator():
    for i in range(5):
        yield i*i

generator = my_generator()

l = list(generator)
print(l)