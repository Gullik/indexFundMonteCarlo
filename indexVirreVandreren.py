"""

A small script to simulate an index fund in a static stock market, with stock
movement simulated as random walkers.

Gullik Vetvik Killie
gullik.killie@gmail.com

"""

import numpy as np
import matplotlib.pyplot as plt

def sellStocks(portfolio, stockMarket):

    """
        Sells all the stocks for the current value
    """

    holdings = np.sum(portfolio[1]*stockMarket[portfolio[0]])

    return holdings


def buyStocks(holdings, portfolio, stockMarket):
    """
        Sells all stocks at current values, then uses the total value to rebuy the top 10 stocks
    """

    indexes = np.argpartition(stockMarket, -10)[-10:]

    newStocks = (0.1*holdings)/stockMarket[indexes]

    return [indexes, newStocks]


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


runs = 1000
investPerformance = np.empty(runs)


for i in range(runs):
    # Create portfolio and total stock market
    stocks = 10000
    steps = 1000

    print i


    stockMarket = np.ones(stocks)
    portfolio = [x for x in range(int(stocks*.1))],[ 1. for x in range(int(stocks*.1))]


    holdings = np.empty(steps)
    totMarket = np.empty(steps)


    for n in range(steps):

        stockMarket     = virreVandrer(stockMarket)
        holdings[n]     = sellStocks(portfolio,stockMarket)
        portfolio       = buyStocks(holdings[n], portfolio, stockMarket)
        totMarket[n]    = np.sum(stockMarket)


    nn = range(steps)

    # plt.figure()
    #
    # plt.plot(nn, holdings/(stocks*.1))
    # plt.plot(nn, totMarket/stocks)
    # plt.legend(['Holdings', 'Total Market'])

    investPerformance[i] = (10*holdings[-1])/totMarket[-1]

# print investPerformance

print("Mean performance: ", np.mean(investPerformance))
print("Variance: ", np.var(investPerformance))


# plt.show()
