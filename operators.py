# operators is a symbol which is used to perform some operation on one or more than one operands and returns a result
# eg : a+b=case
#         where a,b are operands
#         += are operators
#         c is result
# types of operators
# 1. arithmetic operators : They are used to perform mathematical operations on two values. [operators: +,-,*,/,%,//,**]
# 2. assignment operators : These are used to perform assigning and operation along with assigning of vatiables/values.
# [operators: =,+=,-+,*=,/=,//=,%=,**=] 
# 3. comparison operators : They compare two values and returns a boolean value. [operators: ==,!=,>=,<= ]
# 4. logical operators : These are used to compare two conditions [operators: and, or, not]
# 5. bitwise operators
# 6. identity operators : Identity checks whether two values have same address or not. [operators: is and isnot]
'''
1.
a = 5
b = 6
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)

2.
var1 = 25
var1 += 5
print(var1)

var2 = 20
var2 -= 10
print(var2)

var3 = 10
var3 *= 3
print(var3)

var4 = 5
var4 /=5
print(var4)

var5 = 12
var5 **= 2
print(var5)

'''
'''
var6 = 125
var7 = 125.0
print(var6 == var7)  #True

var8 = 125
var9 = '125'
print(var8 != var9) #true
'''
'''
var1 = 4
var2 = 10
print(var1 >= var2)


var1 = 4
var2 = 4
print(var1 >= var2)

var1 = 10
var2 = 20
print(var1 <= var2)

var1 = 54
var2 = '54'
print(var1 == var2)

var1 = '1234'
var2 = '125'
print(var1 < var2) #True because in string it compares word to word here 3 is less than 5 so the condition is true

'''

#logical operation
'''
var1 = 10 != 20
var2 = 5 != 5
print(var1 and var2) #false
print(var1 or var2) # True
print(not var2) # true

a = True
b = False

print(a and b) #false
print(a or b) #true
print(not a) #false
'''
# task : write a program to compare different data types which are supporeted by python and pass them to logical operators.

a = 10 == 10.0
b = 'sunny' != 'jeshwanth'
print(a and b)
print(a or b)
print(not b)

a = 20.56 == 20.00
b = 50 != 50
print(a and b)
print(a or b)
print(not a)


