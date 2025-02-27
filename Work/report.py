# report.py

import fileparse 

def read_portfolio(filename):
    '''
    Opens a given portfolio file and reads it into a list of tuples.
    '''
    with open(filename) as lines:
        return fileparse.parse_csv(filename, select=['name','shares','price'], types=[str,int,float])
    
def read_prices(filename):
    '''
    Reads a set of prices into a dictionary where the keys of the dictionary are the stock names and the values in the dictionary are the stock prices.
    '''
    with open(filename) as lines:
        return dict(fileparse.parse_csv(filename, types=[str,float], has_headers=False))
    
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


def print_report(reportdata):
    '''
    Print the report with headers name, shares, price, change and values formatted and aligned.
    '''
    headers = ('Name', 'Shares', 'Price', 'Change')
    print('%10s %10s %10s %10s' % headers)
    print(('-'*10 + ' ') * len(headers))
    for name, shares, price, change in reportdata:
        dollar_price = f'${price:0.2f}'
        print(f'{name:>10s} {shares:>10d} {dollar_price:>10s} {change:>10.2f}')


def portfolio_report(portfoliofile, pricesfile):
    '''
    Executes the creation and printing of the report.
    '''
    portfolio = read_portfolio(portfoliofile)
    prices = read_prices(pricesfile)
    report = make_report(portfolio, prices)
    print_report(report)

# portfolio_report('Data/portfolio.csv', 'Data/prices.csv')

def main(args):
    if len(args) != 3:
        raise SystemExit(f'Usage: {args[0]} portfoliofile pricesfile')
    portfolio_report(args[1], args[2])


if __name__ == '__main__':
    import sys
    main(sys.argv)




# Functions not used
def portfolio_cost(portfoliofile, pricesfile):
    '''
    Calculates the cost of a given portfolio.
    '''    
    portfolio = read_portfolio(portfoliofile)
    prices = read_prices(pricesfile)

    # Calculate the total cost of the portfolio
    total_cost = 0.0
    for share in portfolio:
        total_cost += share['shares'] * share['price']
    return total_cost

def portfolio_value(portfoliofile, pricesfile):
    '''
    Calculates the value of a given portfolio.
    '''    
    portfolio = read_portfolio(portfoliofile)
    prices = read_prices(pricesfile)
    
    # Calculate the current value of the portfolio
    current_value = 0.0
    for share in portfolio:
        current_value += share['shares'] * prices[share['name']]
    return current_value
