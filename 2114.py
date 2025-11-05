# sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
# ans = 0
# for i in range(len(sentences)):
#       ans = max(ans, len(sentences[i].split()))
# print(ans)
"""sentences = ["alice    and bob love leetcode"]
ans = 0
for i in range(len(sentences)):
      ans = max(ans, len(sentences[i].split()))
print(ans)"""

sentences = ["alice and bob love leetcode"]
ans=0
for i in range(len(sentences)):
      ch = sentences[i]
      if ch==" ":
            ans = ans + 1
print(ans)

# print(len(sentences.split()))