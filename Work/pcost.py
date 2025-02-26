# pcost.py

import report

def portfolio_cost(filename):
    '''
    Computes the total cost (shares*price) of a portfolio file
    '''
    portfolio = report.read_portfolio(filename)
    return sum([s['shares']*s['price'] for s in portfolio])
    
def main(args):
    if len(args) != 2:
        raise SystemExit(f'Usage: {args[0]} portfoliofile')
    filename = args[1]
    print('Portfolio cost:', portfolio_cost(filename)) 

if __name__ == '__main__' :
    import sys
    main(sys.argv)


# if len(sys.argv) == 2:
#     filename = sys.argv[1]
# else:
#     filename = input('Enter a filename:')

# cost = portfolio_cost(filename)
# print('Total cost:', cost)
