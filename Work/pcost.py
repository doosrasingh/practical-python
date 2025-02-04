# pcost.py
#
# Exercise 1.27
with open('Data/portfolio.csv', 'rt') as f:
    headers = next(f)
    cost = 0
    for line in f:
        row = line.split(',')
        cost += int(row[1]) * float(row[2])
    print('Total cost', cost)
