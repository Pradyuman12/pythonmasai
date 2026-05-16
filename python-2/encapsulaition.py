class Bank:
  def __init__(self,name:str,balance:int):
    self.name:str=name
    #praivet
    self.__balance:int=balance
    #getter
  def get_balance(self):
     print(f"current balance:{self.__balance}")
  def setars(self, new_amount):
     self.__balance=new_amount

  def deposit(self,amount):
      self.__balance +=amount
      print(f"your amount is deposited:{self.__balance}\n")
  def widrole(self,amount):
      if amount>self.__balance:
         print("not amount and insuffisant balance")
      else:
         self.__balance-=amount
         print(f"your amount is widrole:{self.__balance}")



acc=Bank("pradyuman",4000)
acc.deposit(1000)

acc.__balance=10000
acc.widrole(800)
acc.get_balance()