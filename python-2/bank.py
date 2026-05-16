"""class Back_Account():
  def __init__(self,belance):
    self.belance=belance
    

  def deposits(self,amount):
      if amount > 0 :
       self.belance += amount
       print(f"belance:{self.belance} amount:{amount}")

  def widrol(self,amount):
      if 0 < amount <  self.belance:
         self.belance -=amount
         print(f"your belance: {self.belance} wridrol amount:{amount}")
      else:
        print("insufficent belance")


my_Account=Back_Account(1000)
my_Account.deposits(100) 
my_Account.widrol(1200)  """     




"""class person():
  spcefic="hello pradyuman"

  def __init__(self,name):
    self.name=name

  @classmethod
  def gete_specise(cls):
    return cls.spcefic
  print(spcefic)
  
  @staticmethod
  def static(age):
    return age >= 18
  

p1=person()"""





class complex():
  def __init__(self,real,imege):
     self.real=real
     self.imege=imege
    
  def add(self,other):
      return complex(self.real + other.real, self.imege + other.imege)
  
  def display(self):
      sign="+" if self.imege >=0 else "-"
      print(f"{self.real} {sign} {(self.imege)}i")

a=complex(1,3)
b=complex(2,3)
c=a.add(b)
c.display()

    
  
