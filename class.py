"""class emp:
  name="pradyuman"
  age=25
  def show(self):
    print(self.name)
    print(self.age)

e=emp()
print(e.name)
print(getattr(e, "name"))
print(hasattr(e,"name"))
setattr(e,"height",154)

print(getattr(e,"height"))
delattr(emp,"age")"""




"""class student:
  name=""
  gender=""
  age=0
  def self_info(self):
    self.name=input("enter name ")
    self.gender=input("enter gender")
    self.age=int(input("enter age"))

  def display(self):
      print(f"your is {self.name} gender {self.gender} age:{self.age}")


s1=student()
s1.display()
s1.self_info()
s1.display()
"""


"""class Movie:
  def __init__(self,movie_name:str,tickt_avlebale:int,total_seats:str):
    self.movie_name= movie_name
    self.tickt_avlebale=tickt_avlebale
    self.seat_price=0
    self.total_seats=total_seats


  def book_seate(self,num_of_tickt:int):
    if num_of_tickt > self.total_seats-self.seat_price:
      print("sorry:not enoght seats avalabile")
    else:
      self.seat_price +=num_of_tickt
      self.total_seats -=num_of_tickt
      print("your seate is booked")
      print(f"your ticket price:{self.seat_price * num_of_tickt}\n")



  def show_seate(self):
    
    print(f"movie:{self.movie_name}")
    print(f"seat avalable:{self.total_seats}")
    print(f"book seate:{self.seat_price}")


movie=Movie("krish",400,100)  
movie.show_seate()
movie.book_seate(70)

movie.show_seate()"""


# inheritens

class Animal:
  def __init__(self,name:str,age:int):
    self.name=name
    self.age=age

    
  def eat(self):
    print("i am eating")

  def sleep(self):
    print("i am sleeping")
  
  def move(self):
    print("i am move")

  def display(self):
    print(f"this is name:{self.name} age:{self.age}") 

class Dog(Animal):
  def __init__(self, name:str, age:int,breed:str):
    super().__init__(name,age)
    self.breed=breed
    print(f"this is breed:{self.breed}")
 
  def bark(self):
    print("i am barking")
  
  def move(self):
    print("he move by four leag")

  
  def display(self):
    print(f"this is name:{self.name} age:{self.age} this is breed:{self.breed}") 


dog =Dog("cherry",5,"indie")
dog.move()




#polymorphism