jewels = "aaaaaA"
stones = "aAAbbb"
ans = 0
for i in range(len(stones)):
      if stones[i] in jewels:
            ans+=1
print(ans)