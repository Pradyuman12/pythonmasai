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

"""def is_prime(nums):
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
    print(f"this is not prime {n}")"""



"""name="reetu"
print(name)

name="tripti"
print(name)"""




"""first="Hello"
second="world"

result=first+" "+second

print(result)
print(first.upper())"""



#first="  hell o   "

#print(first.strip())

"""name="alice"
age=25
srind=f"this is {name},this is {age}"
print(srind)"""

"""pi=3.144578969874475896789

print(f"pi value: {pi:.10f}")"""



"""student=["kalpesh","deepak","rahul","pradyuman"]

city=[]
city.append("dehle")

if not city:
  print("this city is empty")"""



"""number=list(range(10,100,5))
print(number)"""



"""message="thinks,this,makes,a,lot,sense"

words=message.split(",")
print(words)"""

#number=[10,20,40,7,90,1,2,3,4,5]
#print(number[3:7:2])
#print(number[:7])
#print(number[4:])
#print(number[:])
#print(number[-3:])

"""size=len(number)
middle=size//2

first_half=number[0:middle]
second_half=number[middle:]
print(first_half)
print(second_half)"""


"""word=["apple","delhi","gurgaon","chennai","bangalore"]
word.sort()
print(word)"""


"""original=[5,1,2,3,4]
copy=original

print(original)
print(copy)

original.sort()

print("===========")
print(original)
print(copy)"""



"""words=["apple","delhi","goa","gurgaon"]
for i,word in enumerate(words):
  print(f"{i}:{word}")"""


#names=["kalpesh","harole","tripti","Reetu"]
"""marks=[60,58,90,78]

for name,mark in zip(names,marks):
  print(f"{name}:{mark}")"""


#names=("kalpesh","harole","tripti","Reetu")

"""print(names)
names.append()
print(names)"""


"""def get_coodinater():
  return 10,3

ans=get_coodinater()
print(ans)
print(type(ans))
"""


"""nums=int(input("enter number"))

if nums%2==0:
  print(f"this is even {nums}")
else:
  print(f"this is odd {nums}"""


"""nums_1=int(input("enter number"))
nums_2=int(input("enter number"))
nums_3=int(input("enter number"))


if nums_1>nums_2 or nums_1>nums_3:
  print(f"this is large number {nums_1}")
elif nums_1<nums_2 or nums_2>nums_3:
  print(f"this is large number {nums_2}")
elif nums_3>nums_1 or nums_3>nums_2:
  print(f"this is large number {nums_3}")
else:
  print("every number evcele")"""




"""def is_prime(nums):
  if nums <=1:
    return False
  for i in range(2,nums):
    if nums%i==0:
      return False
  
  return True
  
nums=[3,4,5,6]

for n in nums:
   if is_prime(n):
     print(f"this is prime number {n}")
   else:
     print(f"this is not prime number {n}")"""






"""num=int(input("enter number "))
fect=1
for i in range(1,num+1):
    fect=fect*i

print(fect)"""


"""def fectoril(num):
  if num ==1 or num==0:
     return 1
  
  return num*fectoril(num-1)

num=int(input("enter number"))
print(fectoril(num))"""

"""def fibo(num):
  if num==1 or num==0:
    return num
  return  fibo(num-1) + fibo(num-2)

num=int(input("enter number"))
print(fibo(num))"""

"""def revers(strings):
    strings = list(strings)
    left =0
    right=len(strings)-1
    while left < right:
     strings[left],strings[right]=strings[right],strings[left]
     left +=1
     right-=1
     return "".join(strings)


print(revers("python"))"""


"""def palindrom(s,left,right):
  if left >right:
    return False
  if s[left] !=s[right]:
    return False
  
  return True
  
  
s="madam"
print(palindrom(s,0,len(s)-1))"""


"""def vowales(s):
  vowal="aioueAIOUE"
  sum=0
  for i in s:
    if i in vowal:
      sum +=1

  return sum 

  
s="hello pradyuman"
print(vowales(s))"""



"""def large_num(nums):
  larger=nums[0]
  for num in nums:
    if num > larger:
      larger=num
  return larger


nums=[1,2,3,4,5]
print(large_num(nums))"""




"""num =[1,2,3,2,4,5,6,3]

result=[]

for i in num:
  if i not in result:
    result.append(i)


print(result)"""


"""def merge_sort(list_1,list_2):
  
  result=[]
  i=0
  j=0
  while i<len(list_1) and j<len(list_2):
    if list_1[i]<list_2[j]:
      result.append(list_1[i])
      i +=1
    else:
      result.append(list_2[j])
      i +=1

      while i<len(list_1):
        result.append(list_1[i])
        i +=1


        while j <len(list_2):
          result.append(list_2[j])
          j +=1
        return result

      

list_1=[1,2,4,6,7,8]
list_2=[3,4,8,9,5,6]
print(merge_sort(list_1,list_2))"""

"""def revers(string):
  string=list(string)
  left=0
  right=len(string)-1
  while left<right:
    string[left],string[right]=string[right],string[left]
    left +=1
    right-=1

    return "".join(string)



string="python"
print(revers(string))"""

"""def is_prime(num):
  if num<=1:
    return False
  for i in range(2,num):
    if num%i==0:
      return False
    
    return True

  
print(is_prime(8))"""


"""def dublicat(nums):
  sum=[]
  for i in nums:
    if i not in sum:
      sum.append(i)
  return sum
  
dub=[1,2,3,4,5,6,4,5,2]
print(dublicat(dub)) """


"""def fibonachi(num):
  if num==1 or num==0:
     return num
  return fibonachi(num-1) + fibonachi(num-2)

print(fibonachi(10))"""




"""def merge_sort(list_1,list_2):
   result=[]
   i=0
   j=0
   while i< len(list_1) and j< len(list_2):
      if list_1[i]<list_2[j]:
       result.append(list_1[i])
       i +=1
       
      else:
        result.append(list_2[j])
        j +=1

   while i <len(list_1):
     result.append(list_1[i])
     i +=1
   while j <len(list_2):
     result.append(list_2[j])
     j +=1

   return result

list_1=[1,2,3,4]
list_2=[5,6,7,8]
print(merge_sort(list_1,list_2))"""

"""def second_large(nums):
  large=nums[0]
  for num in nums:
    if num > large:
      large=num-1
  return large


nums = [1,2,3,4,5,6]
print(second_large(nums))"""





"""def revers_string(string):
  string=list(string)
  left=0
  right=len(string)-1
  while left < right:
    string[right],string[left]=string[left],string[right]
    left +=1
    right -=1
  return string
  
string="python"
print(revers_string(string))"""

"""def is_prime(num):
  if num <=1:
    return False
  for i in range(2,num):
    if num%i==0:
      return False
  return True

num=4
print(is_prime(num))"""


"""def dublicate(num):
  result=[]
  for i in num:
    if i not in result:
      result.append(i)
  return result

num=[1,2,3,4,1,2,5,6,6]
print(dublicate(num))"""



"""num=5
sum=1
for i in range(1,num+1):
    sum=sum*i

print(sum)"""



"""def fibonacci(num):
  if num==1 or num==0:
    return num
  return fibonacci(num-1)+fibonacci(num-2)

num=10
print(fibonacci(num))"""

"""def large(num):
  large=num[0]
  for i in num:
    if i>large:
      large=i
  return large

num=[40,50,10,20,62,52]
print(large(num))"""


"""def vowals(num):
  vole="aioueAIOUE"
  count =0
  for i in num:
   if i in vole:
    count +=1
  return count

num="programms"
print(vowals(num))"""


"""def merge1_sort(list_1,list_2):
  result=[]
  i=0
  j=0
  while i<len(list_1) and j < len(list_2):
    if list_1[i] < list_2[j]:
      result.append(list_1[i])
      i+=1
    else:
      result.append(list_2[j])
      j+=1

    while i<len(list_1):
        result.append(list_1[i])
        i +=1

    while j<len(list_2):
          result.append(list_2[j])
          j+=1

    return result

list_1=[1,2,3]
list_2=[4,5,6]
print(merge1_sort(list_1,list_2))"""


"""def palindrom(string,left,right):

  while left< right:
    if string[left] != string[right]:
       return False
    
    left +=1
    right -=1
  
  return True

s="madem"
print(palindrom(s,0,len(s)-1))"""
  
"""class Test:
    def __init__(self):
        print("Hello")

obj = Test()"""




#print(bool([]), bool(" "), bool(0))
  
"""class Reteangale:
  def __init__(self,lenght,width):
    self.lenght=lenght
    self.width=width

  def area(self):
    return self.lenght*self.width
  def widht(self):
    return 2*self.lenght*self.width
  

obj=Reteangale(10,15)
print(obj.area())
print(obj.widht())"""   


"""class student:
  def __init__(self,name ,marks):
    self.name=name
    self.marks=marks
  
  def display(self):
    print(f"name:{self.name} marks:{self.marks}")


dis=student("pradyuman",58)  
dis.display()"""


"""class Banck:
  def __init__(self,name,balance):
    self.name=name
    self.balance=balance
    print(f"my balance {self.balance}")
  def deposite(self,diposit):
    self.balance +=diposit
    print(f"your current  balance is :{self.balance}")
    
  def widrol(self,widrol):
    self.balance -=widrol
    print(f"your balance is {self.balance}")


bancks=Banck("pradyuman",100000)
bancks.deposite(100000)
bancks.widrol(50000)"""
    
    
"""class Animals:
  def sound(self):
    print(f"dog is sleeps")
  


class Dog(Animals):
  def bark(self):
    print("dog is barks")

dog=Dog()
dog.bark()
dog.sound()"""






  
    
















  
  
  




































      









  
  
      
      







  


























