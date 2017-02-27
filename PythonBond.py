class Bond(object):
    class Bond(object):
        def __init__(self, rate, price, amount, maturity):
            self.rate = rate
            self.price = price
            self.amount = amount
            self.maturity = maturity
            # Add your method here!

        def description(self):
            print(self.rate)
            print(self.amount)
            print(self.maturity)
            print(self.price)

        def simulation(self):
            for i in range(102):
                self.price = self.amount / (1 + self.rate) ** i
            # self.amount+= 564
            print(self.price)

            # def getAlive(self):
            # return self.alive

    short_term = Bond(0.01, "", 1000, 2)

    short_term.description()

    long_term = Bond(0.03, "", 3000, 5)

    long_term.description()

    short_term.simulation()
    long_term.simulation()

