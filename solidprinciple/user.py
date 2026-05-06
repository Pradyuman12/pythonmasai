class User:
  def __init__(self,name,age,email):
    self.name=name
    self.age=age
    self.email=email

  def get_user_info(self):
    print(f"{self.name,} user age {self.age} email: {self.email}")

  def is_adult(self):
    return self.age >18


  

   
    