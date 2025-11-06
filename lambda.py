
sqr=lambda a:a*a
print(sqr(5))

#write a lambda function to check even or odd

evenOdd=lambda num:"even" if num%2==0 else "odd"
print(evenOdd(4))

#to convert into celsius to farenhet




#lambda fun with sort()
names=["Jeshwanth","Vishal","Ganesh","mahesh"]
names.sort(key=lambda name:len(name))
print(names)

#Lambda with map() fun

list1=[1,2,3, 4,5]
sqlist=list(map(lambda num: num**2, list1))
print(sqlist)

#Lambda with filter function
list2=[1,2,3,4,5,6,7,8,9,10]
filterfun=list(filter(lambda num:num%2==0, list2))
print(filterfun)

#reduce function with lambda
from functools import reduce
list1=[1,2,3,4,5]
redFun= reduce(lambda num1, num2: num1-num2, list1)
print(redFun)

# task
# names=["Jeshwanth Tuljagari","Ganesh Yadav","Vishal Yadav","Malli Reddy"]
# o/p=["JT","GY","VY","MR"]

name="Jeshwanth"
rev=""
for word in name:
      rev=word+rev
print(rev)

names=["Jeshwanth","Sunny","Vishal"]
li1=[]
for words in names:
      rev=""
      for ch in words:
            rev=ch+rev
      li1+=[rev]
print(li1)

      
      

