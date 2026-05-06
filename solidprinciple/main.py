# single responsibility principle
from user import User
from userRepisetry import UserRepisetry

user_info=User("pradyuman",30,"inforcyw12gmail.com")
user_data=UserRepisetry("userdb","root","root")

user_info.get_user_info()
user_data.save_data_baise(user_info)