"""li = [1,2,3,4,5,20,15]
for i in range(len(li)):
      print(sum(li))
      break"""
#leetcode problem 3110
s = "hello"
ans = 0
for i in range(len(s)-1):
      a = ord(s[i])
      b = ord(s[i+1])
      temp = abs(a-b)
      ans = ans + temp
print(ans)