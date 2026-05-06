from abc import ABC ,abstractmethod

"""class payment:
  def pay(self , payment_method,amount):
    if payment_method == "UPI":
      print(f"Your amount is transpar {amount}")
      print("upi transction finished")

    elif payment_method == "creadit-card":
      print(f"your amount is transpar {amount}") 
      print(f"creadit card transction finished")

    elif payment_method == "net-bancking":
      print(f"your amount is transpar {amount}") 


pay=payment()
pay.pay("creadit-card",500)"""


"""class payment(ABC):
    @abstractmethod
    def pay(self, amount:int):
     pass
  
class upimethod(payment):
    def pay(self, amount:int):
     print(f"this is upi payment method amount:{amount}")


class debitemethod(payment):
   def pay(self, amount:int):
      print(f"this is debit payment method amount:{amount}")

class creaditmenthod(payment):
   def pay(self , amount:int):
      print("this is  creadit payment methon amount :{amount}")

class procces_method:
   def paymant(self, payment_procces:"upimethod",amount:int):
      payment_procces.pay(amount)
           
debit=debitemethod()
credit= creaditmenthod()

proc=procces_method()

proc.paymant(debit,500)"""
#lsp
class sevingAccount(ABC):
  def __init__(self,balance):
    self.balance=balance
    
  

  @abstractmethod
  def deposit(self):
    pass
  
  def widrole():
    pass

class Accounts(sevingAccount):
  def __init__(self,balance):
    super().__init__(balance)

  def widrole(self,amount):
    if self.balance<amount:
      print("insufficent balance:{amount}")
    else:
      self.balance -=amount
      print(f"your current balance :{self.balance}")

  def deposit(self,amount):
    self.balance +=amount
    print(f"your current balance:{self.balance}")




class fixAccount(sevingAccount):
  def __init__(self,balance):
    super().__init__(balance)

  def widrole(self,amount):
    raise Exception("cannot widrole fd")

  def deposit(self,amount):
    self.balance +=amount
    print(f"your current balance:{self.balance}")

"""s=Accounts(1000)
s.deposit(1000)
s.widrole(1500)"""

f=fixAccount(10000)
f.deposit(1000)
f.widrole(1000)


        
     



