# we use on polynomial functions and signal processing topics

com1 = 2 + 3j
com2 = 5 + 10j
print(com1) #prints full number
print(type(com1)) # prints type
print(com1.real) # prints real number of a complex number (2 is real number)
print(com1.imag) # prints imaginary number of a complex number (3 is imaginary number)
print(com1+com2)
print(com1-com2)
print(com1*com2)
print(com1/com2)
# print(com1%com2) unsupported operand type for %
# absolute function
print(abs(com1))

#type casting

a = 10
b = 20
print(complex(a,b)) # prints 10+20j
