# names=["chandini", "uday", "sahithi","shreya","sathipandu"]

# #task: print only the first character of every value from above list
# for i in names:
#       print(i[len(i)//2])


# n1="sunny"
# n2="pree"
# print(n1*n2)

# tup1=("sunny")
# print(len(tup1))

# set={"bunny","sunny"}
# for i in range(len(set)):
#       print(set[1])

# list1=['swaroop','sunny','bunny','bhai']
# for i in range(len(list1)):
#       print(list1[i])

# to use list[i] we need to use range and len function without this if we give only list1
#in thr for loop it gives error in that cases we need to use only i

"""while loop:
      we use while loop when we dont know how many times a loop  must iterate.
      we pass a condition to while loop and the loop iterates a s long as the confition is true
      make sure that the condition gives to the while loop is turned into flase at some point.or else it will
      be turned into a infintie loop"""

# count = 10
# while count>=1:
#       print(count)
#       count-=1
# print("loop completed")


#task2: print individual vales in a list using while loop
"""list=['swaroop','sunny','bunny','bhai']
count=0
length=len(list)
while count<length:
      print(list[count])
      count+=1"""
"""flag = True
i = 10
while flag == True:
      print(i)
      i-=1
      if i==5:
            flag=False
            print("loop excited at i=5")"""




#whrite a while loop to check wheter the given credentials are matching or not
#break statment

"""user_name="Jeshwanth yadav"
pass_word="jeshwanth955"
while True:
      username=input("Enter your name: ")
      password=input("Enter you password: ")
      if username==user_name and password==pass_word:
            print("login succesful")
            break
      else:
            print("invalid details")"""

"""for i in range(3):
      print(i,"i am outside loop")
      for j in range(2):
            print(j,"i am inside loop")"""

# Loop control statements "BREAK"
"""for i in range(1,11):
      print(i)
      if i == 5:
            break"""

# Else with for loop
"""names = ['sunny','bunny','kanni','minni']
for i in names:
      if i == 'bunny':
            print(i, "found")
            break
else:
      print('name not found')"""


#Write a proogram, using while loop such that the loop must break when the user 
# pass the input () else it should print the value passed by the user.
"""while True:
    value = int(input("Enter something: "))
    if value == 0:
      break
    print("you entered: ", value)"""

"""names = ["sunny","minny","bunny","kanni"]
length = len(names)
count = 0
while count<length:
      # name = input("Enter your name: ")
      if names[count] == "sunny":
            print("found")
            break
      count+=1

else:
      print("Name not found")"""

#task: do the same username problem with using user name and password using while loop only



"""user_name="Jeshwanth yadav"
pass_word="jeshwanth955"
while True:
      username=input("Enter your name: ")
      if username == user_name:
            print("enter your password")
            while True:

                  password=input("password: ")
                  if password == pass_word:
                        print("login sucessful")
                        break
                  else:
                        print("wrong password")
            
      else:
           print("wrong username")"""

#Continue statements in loops condition 

#Continue:it is used to restart the loop

"""for i in range(1,11):
      if i%2!=0:
            continue
      print(i)"""

# Task for continue: write a program to print only positive numbers using continue
"""n = int(input("Enter a number: "))
count=0
for i in range(n):
      if i<0:
            continue
      print(i)"""

'''list1=[]
for i in range(-5,5):
      if i<=0:
            continue
      list1+=[i]
for i in list1:
      print(i)'''

#Take a list of all days in a week, and print only working days and skip the weekends(i.e.
#  saturday and sunday)

"""week=["monday","tuesday","wednesday","thrusday","friday","saturday","sunday"]
for i in week:
      if i=="saturday" or i=="sunday":
            continue
      print(i)"""

"""days=["monday","tuesday","wednesday","thrusday","friday","saturday","sunday"]
weekends=["saturday","sunday"]
for i in days:
      if i in weekends:
            continue
      print(i)"""

#pass statements is used to pass the condition when were not aware if the code which means 
# we skip the part so that we can write the code whenever we know the code

days=["monday","tuesday","wednesday","thrusday","friday","saturday","sunday"]
weekends=["saturday","sunday"]
workingdays=[]
for i in days:
      pass
print(workingdays)

            
      
      


    

