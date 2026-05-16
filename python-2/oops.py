"""class student:
  def __init__(self,name,RollNo,marks):
    self.name=name
    self.RollNo=RollNo
    self.marks=marks

  def display(self):{
      print(f"name:{self.name} Roll no :{self.RollNo} markes:{self.marks}")
    }
    
s1=student("rahul",45,78)
s1.display()"""


"""class banck():
  def __init__(self,name,balance):
    self.name=name
    self.balance=balance

  def deposit(self,amount):
    self.balance +=amount
    print(f"your balance {self.balance}")
  
  def widrol(self,widrols):
    if self.balance >= widrols:
     self.balance -=widrols
     print(f"your balance {self.balance}")
    else:
      print(f"you can not widrole {self.balance}")
    
    
  def check_balance(self):
    print(f"your balance {self.balance}, name:{self.name}")

b_1=banck("pradyuman",500000)
b_1.check_balance()
b_1.deposit(100000)
b_1.widrol(200000)"""

"""class person:
  def __init__(self,name,age):
    self.name=name
    self.age=age
  
  def show_details(self):
    print(f"name:{self.name} age:{self.age}")
  
class Teacher(person):
  def __init__(self, name, age,subject,selery):
    super().__init__(name, age,)
    self.subject=subject
    self.selety=selery
    
  def show(self):
    print(f"subject:{self.subject} selery:{self.selety}")


teacher=Teacher("pradyuman",45,"math",45000)
teacher.show_details()
teacher.show()"""

class rectengle:
  def __init__(self,l,b):
    self.l=l
    self.b=b
  def area(self):
    return self.l*self.b
  def withd(self):
    return 2*self.b+self.l

rect=rectengle(10,20)      
print(rect.area())
print(rect.withd())