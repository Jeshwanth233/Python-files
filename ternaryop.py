
# MAJOR OR MINOR
"""def category(age):
      return "Major" if age>18 else "Minor"
print(category(23))
print(category(17))"""

#EVEN OR ODD
"""def evenodd(num):
      return "Even" if num%2==0 else "ODD"
print(evenodd(6))"""

#Ternary with loops
"""list1=[1,2,3,4,5,6,7,8]
evenodd=["even" if n%2==0 else "ODD" for n in list1]
print(evenodd)"""


"""list1=[0,1,2,-3,4,5,6,7,8]
a=["zero" if n==0 else "not Zero" if n<0 else "invalid" for n in list1]

print(a)"""

#Grades based on the marks using ternary operator
"""marks=int(input("Enter you marks: "))
result='A' if marks>=90 else "B" if marks>=80 else "C" if marks>=60 else "Fail"
print(result)"""

def good_morning():
      return "Hello Good morning"
def good_afternoon():
      return "Hello Good afternoon"
time = int(input("Enter the tym: "))
greetings=good_morning() if time<12 else good_afternoon()
print(greetings)
