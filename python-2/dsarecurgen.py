



"""def greet(count):
    if count==987:
     return
    print("hello")
    greet(count + 1)

greet(0) """  

"""def greet(count):
  
  if count==4:
    return
  greet(count+1)
  print("pradyuman")

greet(0)"""

count = 0

def greet():
    global count
    if count == 4:
        print("Hello")
        count +=1

greet()