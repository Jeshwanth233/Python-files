"""
list1=[1,2,3,4,5,6,7,8,9,10]
#write a program using function with parameters to return the 
#sum of all the digits inthe above list

def sum(list1): #Declaring a function named sum
      num1=0    #initializing a variable to calculate the sum
      for i in list1: #using for loop to iterate over the sequence 
            num1=num1+i #adding each individual num from the list to the variable
      return num1  #returing the calculated sum
print(sum(list1))"""

"""list1=["Jeshwanth",2,3,4,"sunny",6,"Bunny",8,9]
def fun(list1):
      for i in list1:
            
fun(list1)"""

"""num1=int(input("Enter a num: "))
def prime(num1):
      if num1>1:
            for i in range(2,num1):
                  if num1%i==0:
                        return "Not Prime"
                  else:
                        return "Prime"
      else:
            return "Negative number"
print(prime(num1))
      """

"""str1="Jeshwanth"
rev=""
for i in str1:
      rev=i+rev
print(rev)"""

li1=["jeshwanth", "sunny", "Bunny", "Vishal"]
list2=[]                      #Took a empty list to add the rev words
for word in li1:              #using for loop for iteration to get words in the list                 
      rev=""                  #took a rempty string to rev the char
      for ch in word:         #again using a loop took char from words
            rev=ch+rev        #now storing the rev characters in rev
      list2+=[rev]       #appending the rev char to the empty list
print(list2)

#Write a program to check palindrome of a number and string using two functions,
#and comment out the logic in it, also document the two functions using docstrings..
            


