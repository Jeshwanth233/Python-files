"""list1=["Jeshwanth", "Ganesh", "Vishal", "Manish"]

# print(dict(enumerate(list1)))

dic1={"name":"Jeshwanth","age":22}
print(dict(enumerate(dic1.items())))"""

# Zip()

# names=["Jeshwanth", "Ganesh", "Vishal", "Manish"]
# marks=[99,98,97,86]
# branch=["ECE","EEE","CSE","IT"]


# print(list(zip(names, marks, branch)))

# another way

# for names, marks, branch in zip(names, marks, branch):
#       print(f"{names} has scored {marks} from {branch}")


# mar=list(zip(marks, branch))
# print(dict(zip(names, mar)))

# o/p: {'Jeshwanth':(99,'ECE'),......}

names=["Jeshwanth", "Ganesh", "Vishal", "Manish"]
marks=[99,98,97,86]
branch=["ECE","EEE","CSE","IT"]
res={}
for i in range(len(names)):
      res[names[i]]=(marks[i],branch[i])
print(res)
            


