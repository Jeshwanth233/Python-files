"""n=int(input("enter your number: "))
a=0
for i in range(1,n+1):
      print(i,end="")"""

"""n=int(input("enter your number: "))
a=0
for i in range(1,n+1):
      a+=i
print(a)"""

"""n=int(input("enter your number: "))
if n%2==0:
      print("even")
else:
      print("odd")"""

"""n=int(input("enter your number: "))
fac=1
for i in range(1,n+1):
      fac*=i
print(fac)"""

"""n=int(input("enter your number: "))
rev=0
length=len(str(n))
for i in range(length):
      a=n%10
      rev=rev*10+a
      n=n//10
print(rev)"""

"""
n=int(input("enter your number: "))
rev=0
while n>0:
      rev=rev*10+n%10
      n=n//10
print(rev)
"""
"""
n = int(input("Enter a number: "))
if n > 1:
    for i in range(2, n):
        if n % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")
else:
    print("Not Prime")"""

"""
n = int(input("Enter a number: "))
for i in range(2,n+1):
      for j in range(2,i):
            if i%j==0:
                  break
      else:
            print(i)
"""
"""
n = int(input("Enter a number: "))
a,b=0,1
for i in range(n):
      print(a,end="")
      a,b=b,a+b"""


"""s = input("Enter a string: ")
rev = s[::-1]
print(rev)"""
"""
import math
num = 25
print("Square root:", math.sqrt(num))
print("2 raised to 3:", math.pow(2, 3))
"""

li1=[1,2,5,7,8,9,10,11,12,13]
li2=[]
for i in li1:
      if i>1:
            for j in range(2,i):
                  if i%j==0:
                        
                        break
            else:
                  li2.append(i)
print(li2)
      
      

