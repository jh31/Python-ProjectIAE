#Creation of the class stock
class Stock(object):
    def __init__(self, amount, name, buysize, buydate, selldate, returns ):
        self.amount = amount
        self.name = name
        self.buysize = buysize
        self.buydate = buydate
        self.selldate = selldate
    #Simulate a buy and sell and compute the returns
    def returns(self):
        self.returns = (self.

#importtest10

import pandas as pd

AAPL = pd.read_csv('F:\projet python\Data\AAPL.csv', delimiter= ';')
AXP = pd.read_csv('F:\projet pythons\Data\AXP.csv', delimiter= ';')
FDX = pd.read_csv('F:\projet python\Data\FDX.csv', delimiter= ';')
GOOGL = pd.read_csv('F:\projet python\Data\GOOGL.csv', delimiter= ';')
IBM = pd.read_csv('F:\projet python\Data\IBM.csv', delimiter= ';')
MS = pd.read_csv('F:\projet python\Data\MS.csv', delimiter= ';')
XOM = pd.read_csv('F:\projet python\Data\XOM.csv', delimiter= ';')
YHOO = pd.read_csv('F:\projet python\Data\YHOO.csv', delimiter= ';')
ABCD = pd.read_csv('F:\projet python\Data\ABCD.csv', delimiter= ';') # pense à renommer le fichier 'NOK'

print('AAPL')
print(AAPL)
print('AXP')
print(AXP)
print('FDX')
print(FDX)
print('GOOGL')
print(GOOGL)
print('IBM')
print(IBM)
print('MS')
print(MS)
print('XOM')
print(XOM)
print('YHOO')
print(YHOO)
print('NOK')
print(ABCD)
