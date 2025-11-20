# j = (10,)
# print(type(j))

# j = (10,20,30,30,40,30)
# h = j.index(30)
# p = j.count(30)
# print(j[1:4])


# y=10,
# for x in range(len(y)):
#       print(x)

# for x in [10,20,30]:     #10 20 30
#       print(x)

# dictnory
h = {10,10,10,20,20,40}
print(h)

# set: allows only immutable data types it wont allow the mutable data types
#because set is a mutable data type even set wont allow inside the set datatype because 
#set is mutable as we said set wont allow mutable data type

# l = {10,20}
# # l.add(100) #it add only one value at a time if we want to update more numbers use update function
# l.update({200,300,500})
# print(l)

# l = {10,20,30}
# m = {40,50,60}
# k = (*l,*m)
# print(k)

l = {10,20,30}
l.remove(20) # gives error becz there is no 200
l.pop()       # removes any random number
l.discard(200) # cheks where the given num is there arenot if present it removes if not it skips no error be given 
print(l)

# intersection(): is used to find the common numbers in 2 sets 
#                 we can also use & symbol in place of intersection
#symmetric_difference(): It is used to find the different elements in 2 sets 
k = {10,20,30}
k1 = {10,40,20}
res = k.symmetric_difference(k1) # only differece() is use to fing the different 
#                                  element in the 1st set using 2 ssets
print(res)