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

# a = "_Ajay_Pyhton"
# str=""
# for i in a:
#       if i.isupper():
#             str+="_"+i
#       else:
#             str+=i
# print(str)


"""
a = "_Ajay_Pyhton"

str=""
for i in a:
      if i!="_":          #skip the underScore
            str+=i
       
print(str)    

print(str)"""


"""
a = "listen" 
b = "silent" 
if sorted(a) == sorted(b): 
      print("Anagram") 
else: 
      print("Not Anagram")
"""
"""
j = "PyThOn"
for i in j:
      if ord(i)>=65 and ord(i)<=90:
            d = ord(i)+32
            print(chr(d))
      elif ord(i)>=97 and ord(i)<=122:
            d1 = ord(i)-32
            print(chr(d1))"""


"""
a = "pytthhon"        #{p:1,y:1,t:1,h:1,o:1,n:1} to find the frequency of a string
tem={}
for i in a:
      if i not in tem:
            tem[i]=1
      else:
            tem[i]+=1
print(tem)"""
"""
a = "listen"
b = "silent"
tem={}
tem1={}
for i in a:
      if i not in tem:
            tem[i]=1
      else:
            tem[i]+=1
for j in b:
      if j not in tem1:
            tem1[j]=1
      else:
            tem1[j]+=1
if tem==tem1:
      print("Anagrame")
else:
      print("Not Anagrome")"""

from collections import Counter

a = "listen"
b = "silent"

if Counter(a)==Counter(b):
      print("Anagrame")
else:
      print("Not Anagrame")


h = "sunny@$%123"
digits=letters=special=0
for i in h:
      if i.isalpha():
            letters+=1
      elif i.isdigit():
            digits+=1
      else:
            special+=1
print("alphabets",letters)
print("numeric",digits)
print("special",special)


a = 5
b = 10

temp = a
a = b
b = temp
print("a :",a)
print("b :",b)

      

