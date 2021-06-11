# import numpy as np
from epeparam import *

def wage(labor):
    minwage = 1.3
    rise = 0.1/3000.
    return rise*labor+minwage

def pric(prod):
    minprice = 1.3
    hike = -0.3 / 9000.
    return hike * prod + minprice



# -----------------------------------------
class Firms:
    def __init__(self):
        self.incap = 0.
        self.loan = 0.
        self.labor = 0.
        self.earning = 0.
        self.prod = 0.
        self.outcap = 0.

    def create( self, aaa, bbb, ccc ):
        self.incap = self.incap + aaa
        self.loan = self.loan + bbb
        self.labor = self.labor + ccc

    def decision(self,x):
        # x = [loan+self.incap,labor]
        res = optimize.minimize(earneg(x[0],x[1],loanrate),[3000,3000])
        self.loan = res.x[0]
        self.labor = res.x[1]

    def earneg(self, x, loanrate):
        Z = tecno*(x[0] + self.incap)**theta*x[1]**(1-theta)
        return -(pric(Z)*Z - wage(x[1])*x[1] - x[0]*(1 + loanrate))

    def produce(self, loanrate):
        # self.prod = tecno*(loan + self.incap)**theta*labor**(1-theta)
        prix = pric(self.prod)
        self.outcap = self.incap + (1 - distbratio)*(earn(loanrate))\
                      + (1 - amort)*self.incap

    def profitneg(self, loan, labor, loanrate):
        return -1*earn(loanrate)



    def controle (self):
        print(self.incap, self.loan, self.labor,sel.outcap,\
              'expected profit =',(self.dette + self.deposit) - (self.portfolio + self.prets + self.liquidity))


# ---------------------------------------
class Bank:
    def __init__(self):
        self.dette =0
        self.portfolio =0
        self.prets =0
        self.deposit = 0
        self.liquidity = 0

    def create( self, aaa, bbb , ccc, ddd):
        self.dette = self.dette + aaa
        self.deposit = self.deposit + bbb
        self.portfolio = ccc
        self.prets = ddd
        self.liquidity = self.dette + self.deposit - (self.portfolio+self.prets)

    def emprunte (self, preteur, somme):
        self.dette = self.dette + somme
        self.liquidity = self.liquidity + somme
        preteur.liquidity = preteur.liquidity - somme
        preteur.prets = preteur.prets + somme
    def controle (self):
        print(self.dette, self.deposit, self.portfolio, self.prets, self.liquidity, 'balance=',(self.dette + self.deposit) - (self.portfolio + self.prets + self.liquidity))

class Household:
    labormax = 4000
    wealth = 0
    debt = 0
    labor = 0
    wagepaid = 0
    bank = ""
    deporate = 0
    deposit = 0

    def __init__(self):
        self.wealth = self.wagepaid*self.labor + self.deporate*self.deposit + self.wealth

    def borrow (self, bank, somme):
        self.debt = self.debt + somme
        self.deposit = self.deposit + somme
        bank.liquidity = bank.liquidity - somme
        bank.prets = bank.prets + somme

    def controle (self):
        print(self.debt, self.wealth, self.deposit)
        print(self.debt)


a = Bank()
a.create(350,200,250,200)
bnp=Bank()
bnp.create(300,270,215,255)

a.controle()
bnp.controle()

print('banks cross loans')
a.emprunte (bnp, 75)
bnp.emprunte (a, 95)
a.controle()
bnp.controle()

john=Household()
print('john')
john.borrow(bnp,63)
john.controle()
print('after borrowing')
bnp.controle()

# ibm = Firms()
# ibm.create(8000, 300, 3500)
# ibm.earn(2500,3500, 0.08)
# print(ibm.earning)
# ibm.produce(2500, 3000, 0.09)
# print (ibm.outcap)




