# # Create Account class with 2 attributes - balance & account no.
# # Create methods for debit, credit & printing the balance.

class Account:
   def __init__(self, bal, acc):
      self.balance = bal
      self.account_no = acc

   # Debit method
   def debit(self, amount):
      self.balance -= amount
      print(f"${amount} was debited.")
      print(f"Total balance = ${self.get_balance()}")

   # Credit method
   def credit(self, amount):
      self.balance += amount
      print(f"${amount} was credited.")
      print(f"Total balance = ${self.get_balance()}")

   def get_balance(self):
      return self.balance

acc1 = Account(10000, 1243005)
acc1.debit(1000)
acc1.credit(12500)
acc1.debit(12000)
acc1.credit(41000)