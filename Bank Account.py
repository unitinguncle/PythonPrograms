"""Bank Account
Write a program to automate bank transactions (deposit and withdraw) by creating a class BankAccount to maintain account
balance after every bank transaction. Minimum balance of Rs. 1000 must be maintained for any transaction. Note: (Use Inheritance for 
Minimum Balance Check) """

class BankAccount:
    ## Write Code Here
    def __init__(self,balance, dep_amount, wit_amount):
      self.balance = balance
      self.dep_amount = dep_amount
      self.wit_amount = wit_amount
    
    def deposit(self,dep_amount):
      self.balance = self.balance + dep_amount

    def withdraw(self, wit_amount):
      if(self.balance >=1000):
        self.balance -= wit_amount
      else:
        print("Minimum balance should be 1000 for withdrawl.")

    
class MinimumBalanceAccount(BankAccount):
    ## Write Code Here
    def __init__(self, balance):
      super().__init__(balance, 0, 0)

    def account_balance(self):
      print(self.balance)

    



account = MinimumBalanceAccount(1000)
account.deposit(2500)
account.account_balance()
account.withdraw(500)
account.account_balance()
account.withdraw(1000)
account.account_balance()
account.deposit(1000)
account.account_balance()
account.withdraw(1500)
account.account_balance()
