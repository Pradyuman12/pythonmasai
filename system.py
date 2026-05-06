class Teacher:
    def __init__(self,name:str):
      self.__name:str =name

    def get_name(self):
      return self.__name

    def teacher(self,s:"Student"):
      print(f"{self.__name} is teacher {s.get_name()}")


class Student:
    def __init__(self,name):
     self.__name=name

    def get_name(self):
     return self.__name
    

t1=Teacher("sharma sir") 
s1=Student("rahul") 
t1.teacher(s1)
