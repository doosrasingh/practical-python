# report.py
#
# Exercise 2.4

import csv
import sys

def read_portfolio(filename):
    '''
    Opens a given portfolio file and reads it into a list of tuples.
    '''
    portfolio = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            record = dict(zip(headers, row))
            holding = {
                'name': record['name'],
                'shares': int(record['shares']),
                'price': float(record['price'])
            }
            portfolio.append(holding)
    return portfolio

def read_prices(filename):
    '''
    Reads a set of prices into a dictionary where the keys of the dictionary are the stock names and the values in the dictionary are the stock prices.
    '''
    prices = {}
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                pass
    return prices


def make_report(portfolio, prices):
    '''
    Make a list of (name, shares, price, change) tuples given a portfolio list
    and prices dictionary.
    '''
    rows = []
    for stock in portfolio:
        current_price = prices[stock['name']]
        change = current_price - stock['price']
        summary = (stock['name'], stock['shares'], current_price, change)
        rows.append(summary)
    return rows


# Read data files for portfolio and prices
portfolio = read_portfolio('Data/portfolio.csv')
prices = read_prices('Data/prices.csv')


# Generate report data
report = make_report(portfolio, prices)

# Output the report
headers = ('Name', 'Shares', 'Price', 'Change')
print('%10s %10s %10s %10s' % headers)
print(('-'*10 + ' ') * len(headers))
for name, shares, price, change in report:
    dollar_price = f'${price:0.2f}'
    print(f'{name:>10s} {shares:>10d} {dollar_price:>10s} {change:>10.2f}')
    

# Calculate the total cost of the portfolio
total_cost = 0.0
for share in portfolio:
    total_cost += share['shares'] * share['price']

print('Total cost', f'{total_cost:0.2f}')

# Calculate the current value of the portfolio
current_value = 0.0
for share in portfolio:
    current_value += share['shares'] * prices[share['name']]

print('Current value', f'{current_value:0.2f}')
gain = current_value - total_cost
print('Current gain', f'{gain:0.2f}')
