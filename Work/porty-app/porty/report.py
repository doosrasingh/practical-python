# report.py

from . import fileparse 
from .stock import Stock
from . import tableformat
from .portfolio import Portfolio

def read_portfolio(filename, **opts):
    '''
    Opens a given portfolio file and reads it into a list of tuples.
    '''
    with open(filename) as lines:
        return Portfolio.from_csv(lines, **opts)
    
def read_prices(filename):
    '''
    Reads a set of prices into a dictionary where the keys of the dictionary are the stock names and the values in the dictionary are the stock prices.
    '''
    with open(filename) as lines:
        return dict(fileparse.parse_csv(lines, types=[str,float], has_headers=False))
    
def make_report(portfolio, prices):
    '''
    Make a list of (name, shares, price, change) tuples given a portfolio list
    and prices dictionary.
    '''
    rows = []
    for stock in portfolio:
        current_price = prices[stock.name]
        change = current_price - stock.price
        summary = (stock.name, stock.shares, current_price, change)
        rows.append(summary)
    return rows


def print_report(reportdata, formatter):
    '''
    Print the report with headers name, shares, price, change and values formatted and aligned.
    '''
    formatter.headings(['Name', 'Shares', 'Price', 'Change'])    
    for name, shares, price, change in reportdata:        
        rowdata = [ name, str(shares), f'${price:0.2f}', f'{change:0.2f}' ]
        formatter.row(rowdata)


def portfolio_report(portfoliofile, pricesfile, fmt='txt'):
    '''
    Executes the creation and printing of the report.
    '''
    # Read data files
    portfolio = read_portfolio(portfoliofile)
    prices = read_prices(pricesfile)

    # Create the report data
    report = make_report(portfolio, prices)

    # Print it out
    formatter = tableformat.create_formatter(fmt)
    print_report(report, formatter)


def main(args):
    if len(args) != 4:
        raise SystemExit(f'Usage: {args[0]} portfoliofile pricesfile format')
    portfolio_report(args[1], args[2], args[3])


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
