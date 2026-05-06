from Account import Account
from abc import  abstractmethod
class Widrol(Account):
  def __init__(self, balance):
    super().__init__(balance)
  @abstractmethod
  def widrols(self,amount):
   pass 

  