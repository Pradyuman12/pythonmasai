menu= {
  "pasta":40,
  "selad": 50,
  "Burgar":60,
  "pizza":90,
  "coffie":60,

}

print("welcome to Python Resturante")
print("menu  pasta-50\n selad-50\n Burgar-60\npizza-90\ncoffie-60")

oders_menu=0
oder=input("enter your oders=")
if oder in menu:
  oders_menu += menu[oder]
  print(f"your oder {oder} has been add succesfully")
else:
  print("this oder connot be given yet ")

other_oder=input('do you want to add more thins (yes/no)=')
if other_oder=="yes":
  oder_1=input("enter your second oder=")
  if  oder_1 in menu:
      oders_menu += menu[oder_1]
      print(f"your oder {oder} has been add succesfully")
  else:
      print("this oder connot be given yet ")
    
print(f"your total amount {oders_menu}")
    




 
