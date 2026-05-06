from Account import Account

class Fixed_deposit(Account):
  def __init__(self, balance):
    super().__init__(balance)

    
  def deposit(self,amount):
    self.balance+=amount
    print(f"this is your currend balance:{self.balance}")