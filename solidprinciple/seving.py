from Widrol import Widrol

class Savings(Widrol):
  def __init__(self, balance):
    super().__init__(balance)

  def deposit(self,amount):
    self.balance+=amount
    print(f"this is your currend balance:{self.balance}")

  def widrols(self, amount):
    if self.balance<amount:
     print(f"insufficent balance:")
    else:
      self.balance -=amount
      print(f"your corrent balance:{self.balance}")
      
