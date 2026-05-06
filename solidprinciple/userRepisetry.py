from user import User
class UserRepisetry:
  def __init__(self,db,user,passwrod):
    self.db=db
    self.user=user
    self.passwrod=passwrod
  

  def save_data_baise(self,user:"User"):
    print(f"{user.name} save databese")

  def delt_data(self,user:"User"):
    print(f"{user.name} deleted databese")  
    
    