"""
a = "python developer"
s1= a.upper()                 #to capital the whole scentence
print(s1)

b = "python developer"
s2 = b.title()                 # to make the starting character capital in every word
print(s2)

c = "python developer"
s3 = c.capitalize()            #makes first character capital in a scentence
print(s3)

d = "pyThoN deVeLoPer"
s4 = d.swapcase()              #changes the capital to small and small to capital
print(s4)

e = "python developer"
s5 = e.replace("python", "java") # replace python to java
print(s5)

f = "python developer"
s6 = f.split()                   #stores every word in a list
print(s6)

g = "abc"                         # if you gave numbers it will give false 
s7 = g.isalpha()     #isnumeric() is used to check wheater the value is numeric
print(s7)              # to check the value is alphabets or not"""

"""a = "Pyhton Developer"
str = ""
for i in a:
      if i.islower():
            print(i,end="")"""
"""
a = "pyhton developer"
str=""
for i in a:
      if i in "aeiouAEIOU":
            str+="*"
      else:
            str+=i
print(str)

a = "pyhton developer"
res=""
for i in a:
      res = i + res
print(res)"""

a = "_Ajay_Pyhton"
# str=""
# for i in a:
#       if i.isupper():
#             str+="_"+i
#       else:
#             str+=i
# print(str)

str=""
for i in a:
      if i!="_":          #skip the underScore
            str+=i
       
print(str)    

print(str)
