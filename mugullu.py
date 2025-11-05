# * * * * * 
# * * * * * 
# * * * * * 
# * * * * * 
# * * * * *   
# r=3
# c=10
# for i in range(r):
#       for j in range(c):
#             print("*",end=" ")
#             if j!=c-1:

#                   print("-",end=" ")
#       print("")
"""r = 4
c = 3
for i in range(r):
      for j in range(c):
            print("*",end=" ")
            # if j!=c-1:                   #for not having spaces in the output

            #       print("-",end="")
      print()"""
"""
# ******
# *    *
# *    *
# ******
r=4
c=40
for i in range(r):
      for j in range(c):
            if i==0 or i==r-1 or j==0 or j==c-1:
                  
                  print("*",end=" ")
            else:
                  print(" ",end=" ")
      print()"""
# c=4
# for i in range(c):
#       for j in range(c-i):
#             print("*",end="")
#       print()

"""#        ****
#       ****
#      ****
#     ****
#    ****
#   ****
#  ****
# ****
n=4
c=7
for i in range(c+1):
      for j in range(c-i):
            print(" ",end="")
      for k in range(n):
            print("*",end="")
      print()"""


"""c=5
for i in range(c):
      for j in range(i+1):
            print("*",end="")
      print()"""

# ****
#  ****
#   ****
#    ****
#     ****
"""
c=7
for i in range(c+1):
      for j in range(i):
            print(" ",end="")
      for k in range(n):
            print("*",end="")
      print()
"""

#     *
#    ***
#   *****
#  *******
# *********
"""
r=9
n=r-1
for i in range(r):
      for j in range(n-i):
            print(" ",end="")
      for k in range(i*2-1):
            print("*",end="")
      print()

"""
# *********
#  *******
#   *****
#    ***
#     *
"""
r=5
for i in range(r):
      for j in range(i):
            print(" ",end="")
      temp=2*r-1-i*2
      for k in range(temp):
            print("*",end="")
      print()
"""
"""
r=5
n=r-1
for i in range(r-1,-1,-1):
      for j in range(n-i):
            print(" ",end="")
      for k in range(i*2-1):
            print("*",end="")
      print()
for i in range(1,r):
      for j in range(n-i):
            print(" ",end="")
      for k in range(i*2-1):
            print("*",end="")
      print()
"""     
# *********
#  *******
#   *****
#    ***
#     *
#    ***
#   *****
#  *******
# ********* 
"""
r=5
n=r-1
for i in range(r-1,-1,-1):
     for j in range(n-i):
           print(" ",end="")
     for j in range(i*2+1):
           print("*",end="")
     print()
for i in range(1,r):
      for j in range(n-i):
            print(" ",end="")
      for j in range(i*2+1):
            print("*",end="")
      print()
"""

#    *
#   * *
#  *   *
# *******
"""
r=4
for i in range(r):
      for j in range(r-1-i):
            print(" ",end="")
      for k in range(i*2+1):
            if k==0 or k==i*2 or i==r-1:
                  print("*",end="")
            else:
                  print(" ",end="")

      print()
"""

# *******
#  *   *
#   * *
#    *
"""
r=4
for i in range(r-1,-1,-1):
      for j in range(r-1-i):
            print(" ",end="")
      for j in range(i*2+1):
            if j==0 or j==i*2 or i==r-1:
                  print("*",end="")
            else:
                  print(" ",end="")
      print()
"""

#      *
#     * *
#    *   *
#   *     *
#  *       *
# *         *
#  *       *
#   *     *
#    *   *
#     * *
#      *
"""
r=6
for i in range(r-1):
      for j in range(r-1-i):
            print(" ",end="")
      for j in range(i*2+1):
            if j==0 or j==i*2 or i==r-1:
                  print("*",end="")
            else:
                  print(" ",end="")
      print()
for i in range(r-1,-1,-1):
      for j in range(r-1-i):
            print(" ",end="")
      for j in range(i*2+1):
            if j==0 or j==i*2 or i==r:
                  print("*",end="")
            else:
                  print(" ",end="")
      print()"""

# 1
# 12
# 123
# 1234
# 12345
"""
n=5
for i in range(n):
      for j in range(1,i+2):
            print(j,end="")
      print()
"""

#     1
#    21
#   321
#  4321
# 54321

n=5
for i in range(n):
      for j in range(n-i-1):
            print(" ",end="")
      for k in range(i+1,0,-1):
            print(k,end="")
      print()



                  
            