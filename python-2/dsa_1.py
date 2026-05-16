import math
"""num=5874

while num>0:
  sum_digit=num%10
  print("this digit",num)
  num=num//10"""
"""def counts(count,num):
  while num>0:
   count +=1
   num = num//10
  return count


print(counts(count=0,num=5487) )"""



"""def palindrome(num,result):
 origel=num
 while num>0:
  id=num%10
  result=(result*10)+id
  num=num//10
  return origel==resul
 
print(palindrome(121,0))"""

 


"""def numberdivide(num):
  result=[]
  for i in range(1,num+1):
      if num%i==0:
       result.append(i)

  return result
  
print(numberdivide(20))"""

"""def squresdived(num):
  result=[]
  for i in range(1, int(math.sqrt(num))+1):
    if num%i == 0:
       result.append(i)
       if num//i != i:
          result.append(num // i)
    result.sort()
  return result
      


print(squresdived(36))"""


"""nums=[1,5,8,1,5,8,7,7,6,2,3,2]

frec_map={}
x=1
for i in range(0,len(nums)):
  if nums[i] in frec_map:
    frec_map[nums[i]] +=1
  else:
    frec_map[nums[i]] =1

print(frec_map[x])"""


  
"""def comperinge(num1,num2):
  counts=0
  for i in num1:
    for j in num2:
        if j==i:
         counts +=1
         break
        
  return counts

print(comperinge(num1=[5,4,9,6,5,12,1,3,4,8],
num2=[5,8,12,23,45,9,7,3,1]))"""

"""num1=[5,4,9,6,5,1,3,4,8]
num2=[5,8,12,23,45,9,7,3,1]

hash_map=[0]*11

for i in num1:
  hash_map[i] += 1
for j in num2:
    if j<1 or j>10:
        print(0)
    else:
        print(hash_map[j])
"""


"""num1=[5,4,9,6,5,1,3,4,8]
num2=[5,8,12,23,45,9,7,3,1]

dec={}

for i in num1:
    if i in dec:
        dec[i] +=1
    else:
        dec[i] =1

for j in num2:
  if j<1 or j>10:
      print(0)
  else:
      print(dec.get(j,0))
"""

"""s="azyxyyzaaaa"
q=["a","b","z","x","y"]

hsa_list={}

for i in s:
  hsa_list[i]=hsa_list.get(i,0)+1
  
for j in q:
  print(hsa_list.get(j,0))"""


"""s="azyxyyzaaaa"
q=["a","b","z","x","y"]
has_map=[0]*26

for i in s:
    index= ord(i)-97
    has_map[index] += 1

for j in q:
    index =ord(j)-97
    print(has_map[index])"""


"""def func(sum, i ,n):
  if i>n:
    print(sum)
    return
  func(sum+i,i+1,n)

print(func(sum=0,i=0,n=10))"""

"""def fecto(n):
    if n == 0 or n==1:
       return 1
    return n*fecto(n-1)

print(fecto(5))"""


"""def revers(n,left=0,right=None):
    if right is None:
        right=len(n)-1
 
    if left >= right:
      return n
  
    n[left],n[right]= n[right],n[left]
  
    return revers(n,left+1,right-1)
    

print(revers([1,2,3,4,5,6]))"""


"""def palindrom(s):
  left=0
  right=len(s)-1
  while left < right:
    if s[left] != s[right]:
      return False
    left += 1
    right -= 1
  else:
    return True
  
print(palindrom(s="madad")) """



# recursion

"""def palindrom(s,left,right):
  
  if left >= right:
    return True
  if s[left] != s[right]:
   return False
  return palindrom(s,left+1,right-1)
     
s="madams"    
print(palindrom(s,0,len(s)-1))"""


#fibonacci

"""def fibo(num):
  if num==0 or num==1:
    return num
  return fibo(num-1) + fibo(num-2)


print(fibo(10))"""






"""def palindrom(s,left,right):
  if left >=right:
    return True
  if s[left] != s[right]:
    return False
  return palindrom(s,left +1,right-1)

s="madam"
print(palindrom(s,0,len(s)-1))"""




"""sorting=[4,5,8,7,9,1,2,3]
n=len(sorting)
for i in range(n):
  for j in range(0,n-i-1):
   if sorting[j] < sorting[j+1]:
    temp=sorting[j]
    sorting[j]=sorting[j+1]
    sorting[j+1]=temp

print(sorting)"""

"""sorting=[4,5,8,7,9,1,2,3]

n=len(sorting)
for i in range(n-2,-1,-1):
  for j in range(0,i+1):
    if sorting[j]>sorting[j+1]:
      sorting[j],sorting[j+1]=sorting[j+1],sorting[j]

print(sorting)"""







"""nums=[3,4,5,6,7,1,2,]

n = len(nums)

for i in range(1,n):
  key=nums[i]
  j=i-1
  while j>=0 and nums[j] >key:
    nums[j+1]=nums[j]
    j-=1
    nums[j+1]=key

print(nums) """ 



"""def merge(num_1,num_2):
    result=[]
    i,j=0,0
    n,m=len(num_1),len(num_2)
    while i < n and j<m:
        if num_1[i]<=num_2[j]:
         result.append(num_1[i])
         i+=1
        else:
         result.append(num_2[j])
         j+=1
   
  
    while i<n:
        result.append(num_1[i])
        i +=1

    while j<m:
            result.append(num_2[j])
            j+=1
    return result
    
def sort_marge(num):
  if len(num)<=1:
     return num
  mid=len(num)//2
  left=num[:mid]
  right=num[mid:]
  num_1 = sort_marge(left)
  num_2 = sort_marge(right)
  return merge(num_1, num_2)

num=[1,2,4,5,1,2,3,8]
print(sort_marge(num))"""

"""def funTarget(nums,target):
 for i in range(0,len(nums)):
  for j in range(i+1, len(nums)):
    if nums[i] +nums[j]==target:
     return [i,j]

 
nums=[1,2,3,4,5,6]
target=9 
print(funTarget(nums,target)  )"""

"""def revesefun(nums):
 left=0
 right=len(nums)-1
 while left < right:
  nums[left],nums[right]=nums[right],nums[left]
  left +=1
  right -=1
  return nums



nums=[1,2,3,4,5]
print(revesefun(nums))"""

"""def largest_Num(nums):
  largest=nums[0]
  for n in nums:
    if n>largest:
      largest=n
  return largest

nums=[15,2,47,58,25,23]
print(largest_Num(nums))
"""


"""def reverse(nums):
  left=0
  right=len(nums)-1
  while left<right:
    nums[left],nums[right]=nums[right],nums[left]
    left +=1
    right -=1
  return nums
  
nums=[1,2,3,4,5,6]
print(reverse(nums))"""


""""def fibo(nums):
  if nums==0 or nums==1:
     return nums
  return fibo(nums-1)+fibo(nums-2)

print(bibo(10))"""


def fecto(nums):
  if nums==1:
    return nums
  return nums*fecto(nums-1)

print(fecto(5))







































    
















  










  

  