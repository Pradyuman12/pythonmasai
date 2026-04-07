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


def task():
  tasks=[]
  total_task=int(input("how meny add task "))
  for i in range(1,total_task+1):
   task_name= input(f"enter task {i}=")
   tasks.append(task_name)

  print(f"your task {tasks}",)
 
  while True:
     opetion=int(input("Enter  1-Add\n2-updeate\n3-delete\n4-viwe\n5-exit/stop"))

     if opetion==1: 
      add=input("add more task=") 
      tasks.append(add)
      print(f"your task {add} add succesfully")
     elif opetion==2:
          upedet_value=input("enter task name you want to upedet=") 
          if upedet_value in tasks :
           up=input("enter new task")
           ind=tasks.index(upedet_value)
           tasks[ind]=up
           print(f"upedet value {up}")
     elif opetion ==3:
        dete_value=input("enter delete value =")
        inds=tasks.index(dete_value)
        del tasks[inds]
        print(f"you are {dete_value} has been deleted")
     elif opetion==4:
         print(f"total tasks= {tasks}")
     elif opetion==5:
        print("you are exited")  
        break
     else:
        print("invalid cridencal") 

  




task()








  

















  










