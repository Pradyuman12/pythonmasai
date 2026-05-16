HISTORY_FILE="History.txt" \

def show_history():
  fils=open(HISTORY_FILE,"r")
  liene=fils.readlines()
  if len(liene) == 0:
    print("no history")
  else:
    for line in reversed(liene):
      print(line.strip())
  fils.close()

def clear_History():
  file=open(HISTORY_FILE,'w')
  file.close()
  print("history clear")


def save_to_History(reverse,result):
  file=open(HISTORY_FILE, 'a') 
  file.write(reverse +"="+ str(result) + "\n")
  file.close()
  
def calculater(user_input):
  part=user_input.split() 
  if len(part) != 3:
     print("invalid input you can enter write inputs")
     return
  
  num1=float(part[0])
  op=part[1]
  num2=float(part[2])

  if op=="+":
      result=num1+num2
  elif op=='-':
      result=num1-num2
  elif op=="*":
      result=num1*num2
  elif op=="/":
     if num2==0:
       print("you can not add zero")
       return
     result =num1/num2
     
  else:
     print("invalid operater use +-/*")
     return
  
  if int(result)==result:
     result=int(result)
  print("Result:",result)
  save_to_History(user_input,result)

 
def main():
   print('==siple calculater type of history ==')

   while True:
      user_input=input("enter calculater -+*/ or command")
      if user_input=="exit":
         print("goodby")
         break
      if user_input=="history": 
         show_history()
      if user_input=="clear":
         clear_History()
      else:
         calculater(user_input)

main()
      
      
   
     
       


