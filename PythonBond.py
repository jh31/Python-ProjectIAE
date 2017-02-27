import matplotlib.pyplot as plt

class Bond(object):
    def __init__(self, rate, price, amount, maturity):
        self.rate = rate
        self.price = price
        self.amount = amount
        self.maturity = maturity

    def description(self):
        print(self.rate)
        print(self.amount)
        print(self.maturity)
        print(self.price)

    def simulation(self):
        list_prices = []
        for i in range(2, 102):
            self.price = self.amount / ((1 + self.rate) ** i)
            # self.amount+= 564

            list_prices.append(self.price)

            #print(self.price)
        print(list_prices)


short_term = Bond(0.01, "", 1000, 2)
short_term.simulation()
long_term = Bond(0.03, "", 3000, 5)
#long_term.simulation()

