data=[4,5,8,7,9,]

left=0
rigth=len(data)-1
traget=9

while left < rigth:
    m=(left + rigth) // 2

    if data[m]==traget:
     print(m)
     break
    if data[m] > traget:
     left=m+1
    else:
     rigth=m-1
else:
   print("not found")
