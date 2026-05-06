class student:
 def __init__(self,name,gred):
  self.name=name
  self.gred=gred
  
 def show_detail(self):
    print(f"name: {self.name} gred: {self.gred}")
   
 def is_passing(self):
   return self.gred >=40


s1=student("alice",88)
s2=student("bob",35)

s1.show_detail()
s2.show_detail()
  

print(f"name: {s1.name} is passing: {s1.is_passing()}")
print(f"name: {s2.name} is passing: {s2.is_passing()}")








