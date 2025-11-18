# 1. Create a list of 5 numbers and print the first and last element.

"""li1 = [1,3,7,9,14]
first = li1[0]
last = li1[len(li1)-1]
print("First number: ",first)
print("Last number: ",last)"""



# 2. Given a list, find the sum of all elements without using the sum() function.

"""li1 = [1,3,7,9,14]
sum1 = 0
for i in li1:
      sum1+=i
      
print(sum1)"""


# 3. Find the largest and smallest number in a list.

"""li1 = [1,3,7,9,14]
smallest = li1[0]
largest = li1[0]
for i in li1:
      if i < smallest:
            smallest = i
      if i > largest:
            largest = i
print("smallest:",smallest)
print("largest: ",largest)"""



# 4. Count how many times a specific element appears in a list.

"""li1 = [1,3,5,5,5,5,7,9,14]
target = 5
count=0
for i in li1:
      if i==target:
            count+=1
print(count)"""




# 5. Reverse a list without using the reverse() function.

"""li1 = [1,3,7,9,14]
rev = []
for i in li1:
      rev = [i] + rev
print(rev)"""


# 6. Check if a list is empty or not.
"""li1=[1,2,3]

if li1 == []:
      print("empty")
else:
      print("not an empty")"""

# 7. Given two lists, concatenate them into a single list without using +.
"""li1=[1,2,3]
li2=[4,5,6]
li3=[]
for i in li1:
      li3.append(i)
for j in li2:
      li3.append(j)
print(li3)"""


# 8. Remove duplicates from a list and print the new list.

"""li1 = [1,3,5,5,5,5,7,9,14]
newList = []
for i in li1:
      if i not in newList:
            newList.append(i)
print(newList)
"""
# 9. Find the second largest number in a list.



num = 121
rev = 0
while num > 0:
      digit = num % 10
      rev = rev*10 + digit
      num//10
if num == rev:
      print("palindrome")
else:
      print("Not a palindrome")

# 10. Check if a particular element exists in a list.



      
