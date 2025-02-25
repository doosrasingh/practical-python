# pcost.py
#
# Exercise 1.27

import csv
import sys

def portfolio_cost(filename):
    cost = 0.0
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)        
        for rowno, row in enumerate(rows, start=1):
            record = dict(zip(headers,row))
            try:
                cost += int(record['shares']) * float(record['price'])
            except ValueError:
                print(f'Row {rowno}: Couldn\'t convert:', row)
    return cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = input('Enter a filename:')

cost = portfolio_cost(filename)
print('Total cost:', cost)
