import matplotlib.pyplot as plt

#Creation of the class Bond
class Bond(object):
    def __init__(self, rate, price, amount, maturity):
        self.rate = rate
        self.price = price
        self.amount = amount
        self.maturity = maturity

    #Definition of the method to compute the price
    def simulation(self):
        #Create a new empty list
        list_prices = []
        #Calculate the price of the bond for 100 years
        if self.maturity == 2:
           for i in range(2, 102):
               self.price = self.amount / ((1 + self.rate) ** i)
               #Add a new price in the list
               list_prices.append(self.price)
           print(list_prices)
           #Plot the Graph
           x = range(2, 102)
           y = list_prices
           plt.plot(x, y)
           plt.title("Short term bond price evolution")
           plt.xlabel("Years")
           plt.ylabel("Price of the bond")
           plt.show()
        else:
            for i in range(5, 105):
                self.price = self.amount / ((1 + self.rate) ** i)
                # Add a new price in the list
                list_prices.append(self.price)
            print(list_prices)
            #Plot the graph
            x = range(2, 102)
            y = list_prices
            plt.plot(x, y)
            plt.title("Long term bond price evolution")
            plt.xlabel("Years")
            plt.ylabel("Price of the bond")
            plt.show()


#Creation of two types of bonds
short_term = Bond(0.01, "", 1000, 2)
short_term.simulation()
long_term = Bond(0.03, "", 3000, 5)
long_term.simulation()

