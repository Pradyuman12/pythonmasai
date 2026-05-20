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

"""class rectengle:
  def __init__(self,l,b):
    self.l=l
    self.b=b
  def area(self):
    return self.l*self.b
  def withd(self):
    return 2*self.b+self.l

rect=rectengle(10,20)      
print(rect.area())
print(rect.withd())"""


""""class Person:
  def __init__(self,name,age):
    self._name=name
    self._age=age

  def set_age_name(self,names,ages):
    self._name=names
    self._age=ages

  def get_name(self):
    print(f"name:{self._name} age:{self._age}")


obj=Person("pradyuman",25)
obj.get_name()
obj.set_age_name("rahul",45)
obj.get_name()"""


"""class Dog:
  def sound(self):
     print(f"soun_1")

class Cat:
   def sound(self):
      print(f"sound_2")



cat=Cat()
dog=Dog()
cat.sound()"""


"""class crcile:
  def __init__(self,redus):
    self.redus=redus

  def area(self):
    return 3.14*self.redus*self.redus
    
crs=crcile(5) 
print(crs.area() ) """


"""nums=[1,2,5,4,7,9]
target=7


for j in range(len(nums)):
    if nums[j]==target:
        print(f"{j}")"""


""""def fec(n):
  if n==1 or n==0:
    return n
  
  return n*fec(n-1)

n=5
print(fec(n))"""
  
"""class Student:
    school = "ABC"

s1 = Student()
print(s1.school)"""



"""def revers(strings):
  strings=list(strings)
  left=0
  right=len(strings)-1
  while left <right:
    strings[left],strings[right]=strings[right],strings[left]
    left +=1
    right -=1
  return "".join(strings)

string="python"
print(revers(string))"""

"""def large(num):
  large=num[0]
  for n in num:
    if n>large:
      large=n

  return large
num=[10,20,30,40,88,90]
print(large(num))"""



"""def palindrom(string,left,right):
  while left>right:
    return False
  if string[left] !=string[right]:
    return False
  return True

string="madams"
print(palindrom(string,0,len(string)-1))"""


"""def vowals(stri):
  vowal="aioueAIOEU"
  count=0
  for i in stri:
    if i in vowal:
       count +=1
  return count

stri="hello"
print(vowals(stri)) """


"""def dublicate(num):
  result=[]
  for i in num:
    if i not in result:
      result.append(i)

  return result

num=[10,20,30,40,40,50,20]
print(dublicate(num))"""



"""class Employee:
  def __init__(self,name,selery):
    self.name=name
    self.selery=selery
   
  def display(self):
      print(f"name:{self.name} selery:{self.selery} depatment:{self.depatment}")
   
class Menager(Employee):
   def __init__(self, name, selery,depatment):
      super().__init__(name, selery)
      self.depatment=depatment
      
   def display(self):
      print(f"name:{self.name} selery:{self.selery} depatment:{self.depatment}")
  
m=Menager("rahul",50000,"It") 
m.display() """  


"""class  Father:
  def telant(self):
    print("you are softwere engineear")


class Mother(Father):
  def skill(self):
    print("you are home mekar")


class Chilled(Mother):
  def chaild(self):
    print(f"chaild not working")


c=Chilled()
c.telant()
c.skill()"""


""""class Banck:
  def __init__(self,name,balance):
    self.name=name
    self.balance=balance
    print(f"current balance:{self.balance} name: {self.name}")
  
  def deposite(self,amont):
    self.balance +=amont
    print(f"balance:{self.balance}")
  def widrole(self,widrol):
    if self.balance>=widrol:
      self.balance -=widrol
      print(f"your balance:{self.balance}")
    else:
      print("insufficent balance")

mony=Banck("pradyuman",500000)

mony.deposite(100000)
mony.widrole(1000000)"""

"""
from abc import ABC ,abstractmethod
class Vehical:
  @abstractmethod
  def start(self):
    pass

 
class Car(Vehical):
  def start(self):
    print("car starting")

class Bike(Vehical):
  def start(self):
    print("bike start")


v=Car()
v.start()

b=Bike()
b.start()"""

 
"""class Person:
  def __init__(self,name,age):
    self.name=name
    self.age=age
 
  def __str__(self):
       return f"name:{self.name} age:{self.age}"
  
p=Person("ram",25)


print(p)"""





"""class Point:
  def __init__(self,x,y):
    self.x=x
    self.y=y

  def __add__(self, other):
   return Point(self.x + other.x,self.y+other.y)
  

p1=Point(2,3)
p2=Point(4,5)
p3=p1+p2
print(p3.x,p3.y)"""
    

"""class Product:
  def __init__(self,name,price):
    self.name=name
    self.price=price
    print(f"product:{self.name} price:{self.price}")

class Card:
  def __init__(self):
    self.products=[]
  def add_products(self,Product):
    self.products.append(Product)

  def remove(self,product_name):
    for product in self.products:
      if product.name==product_name:
        self.products.remove(product)
        print(f"{product_name} this product remove")
        return
      

    print("product not found")

  def show(self):
    total=0

    for product in self.products:
      total +=product.price

    print(f"total price: {total}")




p1=Product("mobail",20000)
p2=Product("acc",2000)

c=Card()
c.add_products(p1)
c.add_products(p2)


c.show()
c.remove("acc")"""
      
    
"""def sum_number(num,traget):
  left=0
  right=len(num)-1
  while left <right:
    total=num[left]+num[right]

    if total == traget:
      return num[left],num[right]
    elif total < traget:
      left +=1
    else:
      right -=1
  
  return -1  


num=[1,2,3,4,5,6,7,8]
print(sum_number(num,11))"""


def dublicat(nums):
  nums.sort()
  left=0
  for right in range(1,len(nums)):
    if nums[left] !=nums[right]:
       left +=1
       nums[left]=nums[right]

  return left+1

nums=["aman","rahul","kajel","pradyuman","john","rahul"]
count= dublicat(nums)
print(nums[:count])










    















  





















        







      