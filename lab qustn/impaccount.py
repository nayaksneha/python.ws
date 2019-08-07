from account import Account
class Impaccount:

    def deposite(self,deposite_amount):
        self.balance = self.balance+deposite_amount
        print(f"the balance is :{self.balance}")


    def withdraw(self,withdraw_amount):
        if self.balance -withdraw_amount<0:
            print("incuficint")
        else:
            self.balance = self.balance-withdraw_amount
            print(f"currnt balnce:{self.balance}")

    def showInfo(self):
        pass

a1= Account("45879","sneha","10000")

a1.deposite(50000)
a1.withdraw(1000)
