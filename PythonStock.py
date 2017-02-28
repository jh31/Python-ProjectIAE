
import pandas_datareader.data as web
import datetime
import matplotlib.pyplot as plt

#Creation of the class stock

class Stock(object):
    def __init__(self, amount, name, buysize, buydate, selldate):
        self.amount = amount
        self.name = name
        self.buysize = buysize
        self.buydate = buydate
        self.selldate = selldate

    #Read the data of a stock from Yahoo database and plot the graph

    def readfromweb(self):
        start = datetime.datetime(2005, 1, 3)
        end = datetime.datetime(2015, 2, 13)
        df = web.DataReader(self.name, 'yahoo', start, end)

        df['High'].plot()
        plt.title(self.name)
        plt.xlabel("Years")
        plt.ylabel("Stock price")
        plt.show()

    def buysimulation(self):
        x = range(1, list_prices.count)
        y = list_prices
        plt.plot(x, y)
        plt.xlabel("Years")
        plt.ylabel("Price of the bond")
        plt.show()

#Creation of the different stocks
AAPL_stock = Stock("", 'AAPL', "", "", "")
AAPL_stock.readfromweb()

AXP_stock = Stock("", 'AXP', "", "", "")
AXP_stock.readfromweb()

FDX_stock = Stock("", 'FDX', "", "", "")
FDX_stock.readfromweb()

GOOGL_stock = Stock("", 'GOOGL', "", "", "")
GOOGL_stock.readfromweb()

IBM_stock = Stock("", 'IBM', "", "", "")
IBM_stock.readfromweb()

KO_stock = Stock("", 'KO', "", "", "")
KO_stock.readfromweb()

MS_stock = Stock("", 'MS', "", "", "")
MS_stock.readfromweb()

NOK_stock = Stock("", 'NOK', "", "", "")
NOK_stock.readfromweb()

XOM_stock = Stock("", 'XOM', "", "", "")
XOM_stock.readfromweb()

YHOO_stock = Stock("", 'YHOO', "", "", "")
YHOO_stock.readfromweb()


