"""
def is used to define function followed with a function name is you want ot call
a function just use the function name you created then it will be called automatically

def name(n,s):
      for i in range(n):
            print(s)

name(3,"bunny")
name(10,"sunny")"""

# def sunny():
#       print("oh! this is you my friend sunny")


# name = input("Enter your name: ")
# print("Hello my name is "+name)
# sunny()

#5 table using functions

"""def table(n):
      for i in range(1,11):
            # print(n,"*",i,"=",n*i)
            # print(str(n)+ " * " + str(i)+ " = " + str(n*i))

table(5)"""


"""def add_num():
      num1 = int(input("Enter a number: "))
      num2 = int(input("Enter another number: "))
      print(num1+num2)
print("The first function name")
add_num()
print("The second function name: ")
add_num()"""
"""def greet(name,program_name):
      print(f'''Hello {name},
            Thank you for registering at 10k coderes,
            Hope you do well in your {program_name}''')

greet("sunny","Python full stack")"""
# greet()

#Write a function to check wheather a person is wligible for loan or not, based on his income 
# and credit score.

"""
def salary(salary, credit_score):
      if salary>=0 and 0<credit_score<=900:
                  if salary>=50000 and credit_score>=800:
                          
            
                        print(f"you are eligible for the loan ")
                  else:
                        print("not eligible")
      else:
            print("Invalid values")

salary(55000,-800)
salary(40000,800)
"""

#Local variable

"""def add():
      a = 10
      b = 20
      print(a+b)
print(a)
add()"""

#non local variable
"""def outer():
      var1="This is in outer function"
      var2="This belongs to var2"
      def inner():
            var1="This is in inner function"
            var2="hellooo"
            print(var2)
      inner()
      print(var1)
outer()"""

#Global function
"""glbvar="This is global value"
def func1():
      print("This is function1: ")
      print(glbvar)
def func2():
      print("This is a nested function")
      def func3():
            print(glbvar)
      func3()
func1()
func2()
"""

"""a=20
def gloDemo():
      global a
      a = 15
      print(a)
gloDemo()
print(a)"""

"""
glvram="sunny"
def fun():
      global glvram
      glvram="bunny"
      print(glvram)
fun()
print(glvram)
"""

#non local keyword
def frdwithparents():
      perforamce="Swathimuthyam"
      
      def frdwithme():
            nonlocal perforamce
            perforamce="Chillar"
            print(perforamce)
      frdwithme()
      print(perforamce)

frdwithparents()


