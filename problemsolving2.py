"""# 1. Check Even or Odd
num = 6
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")

# 2. Divisible by 5 but Not by 10
num = 25
if num % 5 == 0 and num % 10 != 0:
    print("Satisfy")
else:
    print("Not satisfy")

# 3. Biggest Among Two Numbers
a, b = 4, 7
if a > b:
    print("Biggest is:", a)
else:
    print("Biggest is:", b)

# 4. Smallest Among Two Numbers
a, b = 4, 7
if a < b:
    print("Smallest is:", a)
else:
    print("Smallest is:", b)

# 5. Divisible by 2, 3, and 6
num = 18
if num % 2 == 0 and num % 3 == 0 and num % 6 == 0:
    print("Satisfy")
else:
    print("Not satisfy")

# 6. Voting Eligibility
age = 19
if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")

# 7. Student Pass/Fail Based on All Subjects >= 35
maths, physics, chemistry = 40, 36, 30
if maths >= 35 and physics >= 35 and chemistry >= 35:
    print("Pass")
else:
    print("Fail")

# 8. Student Pass if Passed Any One Subject
maths, physics, chemistry = 20, 38, 25
if maths >= 35 or physics >= 35 or chemistry >= 35:
    print("Pass")
else:
    print("Fail")

# 9. Student Pass if Passed Any Two Subjects
maths, physics, chemistry = 40, 20, 36
ans = 0
if maths >= 35:
    ans += 1
if physics >= 35:
    ans += 1
if chemistry >= 35:
    ans += 1

if ans >= 2:
    print("Pass")
else:
    print("Fail")

# 10. Biggest Among Three Numbers
a, b, c = 7, 4, 9
if a > b and a > c:
    print("Biggest is:", a)
elif b > a and b > c:
    print("Biggest is:", b)
else:
    print("Biggest is:", c)

# 11. Smallest Among Three Numbers
a, b, c = 7, 4, 9
if a < b and a < c:
    print("Smallest is:", a)
elif b < a and b < c:
    print("Smallest is:", b)
else:
    print("Smallest is:", c)

# 12. Perfect Square or Not
import math
num = 49
if int(math.sqrt(num)) ** 2 == num:
    print("Perfect square")
else:
    print("Not a perfect square")

# 13. Cars Required for Members (Max 5 per car)
import math
members = 17
cars = math.ceil(members / 5)
print("Cars needed =", cars)

# 14. Second Biggest Among Three Numbers
a, b, c = 10, 25, 18
nums = [a, b, c]
nums.sort()
print("Second biggest:", nums[1])

# 15. Leap Year or Not
year = 2024
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap year")
else:
    print("Not a leap year")"""


# 16. Reverse a string without using built-in methods.


"""name = "Jeshwanth"
rev = ""
for i in name:
      rev = i + rev
print(rev)"""


# 17. Check if a number is prime.

"""num = 11
i = 2
while num > i:
    if num%i==0:
        print("NOT PRIME")
        break
    i+=1
else:
     print("PRIME")"""
"""
num = 7
cou = 0
for i in range(1,num):
    if num%i==0:
        cou+=1
if cou==1:
    print("PRIME")
else:
    print("NOT A PRIME")"""
      




# 18. Return the first non-repeating character in a string.


# 19. Find the missing number in a list of 1 to n.


# 20. Count frequency of characters in a string.


# 21. Remove duplicates from a list without using set.


# 22. Write a program to check if two strings are anagrams.


# 23. Find max and min in a list without built-ins.


# 24. Implement binary search.


# 25. Find the second largest number in a list.


# 26. Rotate an array by k positions.


# 27. Merge two sorted lists into one sorted list.


# 28. Implement a stack using two queues.


# 29. Detect a palindrome without slicing.


# 30. Generate Fibonacci numbers up to 
