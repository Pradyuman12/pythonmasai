"""list=[]
movie=str(input("enter first movie"))
movie1=str(input("enter second movie"))
movie2=str(input("enter tharde movie"))

list.append(movie)
list.append(movie1)
list.append(movie2)
print(list)
"""
"""count=100
while count>=1 :
  print("hello",count)
  count -=1
"""
"""mul=int(input("enter number"))
i=1
while i <=10 :
  print("multiplication :",mul*i)
  i +=1
"""
"""nums=[1,4,9,16,25,36,49,64,81,100]
idx=0
while idx<len(nums) :
  print(nums[idx])
  idx+=1
"""
"""nums=(1,4,9,16,25,36,49,64,81,100)
i=0
x=int(input("search number"))
while i<len(nums):
      if(nums[i]==x):
       print("found index",i)
      i+=1
      """

"""i = 0
while i <= 5:
    if i == 3:
        i += 1
        continue
    print(i)
    i += 1
    """
"""nums=[14,4,7,8,5]

for val in nums :
  print(val)
"""
"""n=5
fcato=1
i=1
while i<=n:
  fcato *=i
  i+=1

print("fectorial", fcato)
"""
"""def calc_sum(a,b):
  return a+b

sum=calc_sum(1,2)
print(sum)"""

"""def averge(a,b,c):
  return (a+b+c)/2
ave=averge(12,4,6)
print(ave)"""
"""cites=["delhi", "gurgaon", "noida", "pune","mumbai","chennai"]
heroes=["thor","ironman", "captain", "shatiman"]

def print_len(list):
   print(len(list))
   
print_len(cites)
print_len(heroes)
"""
"""def usd(amount):
  return amount*83

amounts=int(input("enter amount"))
print(usd(amounts))"""

#num=int(input("enter number"))

"""def even_odd(num):
  if(num%2==0):
   return print("this is  even number")
  else:
   return print("this is odd number")
nums=even_odd(num)
print(nums)"""

"""def show(n):
  if(n==0):
    return
  print(n)
  show(n-1)

show(5)"""

"""def fact(n):
  if(n==1 or n==0):
    return 1
  return fact(n-1)*n

facto=fact(5)
print(facto)"""

"""age=20
license=False

car= age >=18 and license 
print(car)"""


"""name=str(input("enter username"))
passwrod=input("enter passwrod")

if name == "pradyuman":
  print("username found")
if passwrod =="12" :
  print("login succussfull")
  print("welcome to your account")
else :
  print("wrong passwrod")"""



"""price=52
quantity=3
print(f"total: {price*quantity}")
"""

"""class cars:
  def __init__(self):
    print(self)
    print("adding")
  color = "blue"

car1=cars()"""


"""class Student:
  def __init__(self,name ,marks):
    self.name =name
    self.marks= marks

  def get_avg(self):
      sum=0
      for val in self.marks:
       sum +=val
      print("hi",self.name, "your avg score is",sum/3)

s1=Student("tony stark",[99,87,45])
s1.get_avg()
"""


"""age= int(input("enter age"))
license=False

if(age<=18 and license==True):
  print("you are aligible drive car")
else:
  print("you are not aligible drive car")
"""

"""num=100
print(f"{num:6}")"""


"""def chek_age(age):
  if age <= 18:
   return "you are young"
  return "you are old"
  
print(chek_age(46))
print(chek_age(4))"""
"""nubers=[1,2,3,5,6,4,7,8]
nubers[::2]
print(nubers)"""
"""def greet_user1(name ,greeting="hello"):
   return name, greeting

print(f"{greet_user1("rehul")}")"""




"""a=[1,4,7,8]
b=["a","b","c"]

print(list(zip(a,b)))"""

"""t=(1,3,8)
print(t)
t[0].append(2)
print(t)"""

#s=" hello wrold "
#print("reples=",s.replace("wrold","python"))
#print("find chrecter=",s.find("d"))
#print("founds index",s.index("w"))
#print('split',s.split())
"""var = 10
for i in range(10):
    print(i)
    for j in range(2,10,1):
        print(j)
        if var % 2 == 0:
            continue
        else:
            var += 1
print(var)"""

"""for num in range(10, 14):
    for i in range(2, num):
        if num%i == 1:
            print(num)
            break"""


"""def file_demo():
  filename="example.txt"
  with open(filename,"w") as f:
      f.write("hello python:\n")
      f.write("this is file handling demo. \n")


  print("data written to file ")

  with open(filename, "r") as f:
      content=f.read()
      print(content)
  with open(filename, "r") as f:
     for line in f:
        print(line.strip())
     
#append file 
  with open(filename, "a") as f:
     f.write("append a new line . \n")
  print("data appended")

  with open(filename,"r") as f:
     lines=f.readlines()
     print(lines)

  line_to_write=["line 1\n","line 2\n", "line 3\n"]
  with open("multi.txt", "w") as f:
     f.writelines(line_to_write)
  
  with open(filename, "r") as f:
    print("initial position:", f.tell())
    f.read(5)
    print("after reading 5 charts:",f.tell())
    f.seek(10)
    f.close()


file_demo()"""

     
"""def exception_demo():
    try:
     x=int(input("enter a number"))
     y=10/x
     print("result:",y)
    except:
          print("som e error occurred!")

 
exception_demo()"""


"""class Mother:
    def skill(self):
        print("Cooking")

class Father:
    def skill(self):
        print("Driving")

class Child(Mother, Father):
    pass

c = Child()
c.skill()"""




"""
class University:
    def enroll(self):
        print("Enrolled in University")

class CSE(University):
    def specialize(self):
        print("Specializing in Computer Science")

class ECE(University):
    def specialize(self):
        print("Specializing in Electronics")

"""
"""class BankAccount:
    def __init__(self):
        self.balance = 5000

    def deduct(self, amount):
        self.balance -= amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.deduct(amount)
            print(f"Remaining balance: {self.balance}")
        else:
            print("Insufficient funds")

acc = BankAccount()
acc.deduct(200)"""







"""class AgeError(Exception):
    def __init__(self, message, age):
        super().__init__(f"{message}: {age}")
        self.age = age

def verify_age(age):
    if age < 0:
        raise AgeError("Negative age not allowed", age)
    elif age > 120:
        raise AgeError("Age exceeds maximum limit", age)
    return "Valid age"

try:
    result = verify_age(-5)
    print(result)
except AgeError as e:
    print("Caught:", e)
    print("Age value:", e.age)
except ValueError:
    print("Not a number")
finally:
    print("Done")
"""

"""class Movie:
  def __init__(self,movie_name,ticket_price,totle_ticket):
    self.movie_name=movie_name
    self.totle_ticket=totle_ticket
    self.ticket_price=ticket_price
    self.book_ticket=0
  def book_myticket(self,nums_ticket):
    if nums_ticket>self.totle_ticket-self.book_ticket:
      print("sorry enoght ticket availeble")
    else:
      self.book_ticket+=nums_ticket
      self.totle_ticket-=nums_ticket
      print("your ticket is booked successfully")
      print(f"your price is {self.ticket_price*nums_ticket}")

      

  def show_status(self):
     
     print(f"movie name {self.movie_name}")
     print(f"availeble seats:{self.totle_ticket}")
     print(f"totle booked:{self.book_ticket}")

    
b1=Movie("krish",100,400)

b1.show_status()
b1.book_myticket(100)
b1.show_status()"""

"""def vovals(s):
  vowals="aeiouAEIOU"
  sum=0
  for char in s:
    if char in vowals:
      sum +=1

  return sum
  

  

s="hello wrold"
print(vovals(s))"""

"""def largest(nums):
  largest=nums[0]
  for num in nums:
    if largest < num:
       largest=num-1
  return largest

nums=[1,2,3,4,5]
print(largest(nums))"""

def is_prime(nums):
  if nums <=1:
     return False
  for i in range(2,nums):
      if nums%i==0:
       return False
  
  return True


nums=[4,5,7,8,9,]

for n in nums:
  if is_prime(n):
    print(f"this is prime {n}")
  else:
    print(f"this is not prime {n}")









