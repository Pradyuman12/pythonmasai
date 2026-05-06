"""def task():
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

  




task()"""





def add_Task():
  print("==== this is to-do-list ====")
tasks=[]
taks_value=int(input("how menay do you want add task= "))
for i in range(1,taks_value+1):
 task_name=input(f"enter task {i}=")
 tasks.append(task_name)

print(f"this is your task {tasks}")

while True:
 operation=int(input("enter 1-Add\n2-update\n3-delete\n4-viwe\n5-exit"))
 if operation==1:
        add=input("add more task")
        tasks.append(add)
 elif operation==2:
          updete_value=input("enter what do you want update name =")
          if updete_value in tasks:
           up=print("enter new name=")
           ind=tasks.index(updete_value)
           tasks[ind]=up
           print(f"name has been {up} succesfully")
 elif operation ==3:
        delete=input("enter delete name")
        dets=tasks.index(delete)
        del tasks[dets]
        print(f"name has been {delete} deleted")
 elif operation==4:
        print(f"total tasks {tasks}")
 elif operation==5:
        print(f"you are exited")
        break
 else:
        print("invalid creadensile")



add_Task()     
        
        

            
            

   




