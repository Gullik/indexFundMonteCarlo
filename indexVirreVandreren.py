"""

A small script to simulate an index fund in a static stock market, with stock
movement simulated as random walkers.

Gullik Vetvik Killie
gullik.killie@gmail.com

"""

import numpy as np
import scipy as sp

def sellStocks(portfolio, stockMarket):

    """
        Sells all the stocks for the current value
    """

    return value


def buyStocks(portfolio, stockMarket):
    """
        Sells all stocks at current values, then uses the total value to rebuy the top 10 stocks
    """

    return portfolio


def virreVandrer(stockMarket):
    """
        A random walker where each stock has a chance to decrease, or increase by 0.1
    """

    for i in range(len(stockMarket)):

        r = np.random.rand()
        if(r < 0.3):
            stockMarket[i] += 0.1
        if(r > 0.7):
            stockMarket[i] -= 0.1


    return stockMarket


# Create portfolio and total stock market
stockMarket = np.ones(100)
portfolio = np.ones([2,10])
portfolio[0,:] = [x for x in range(10)]



for t in range(100):

    stockMarket = virreVandrer(stockMarket)


print(np.sum(stockMarket))

print(stockMarket)
