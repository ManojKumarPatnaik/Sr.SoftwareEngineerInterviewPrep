from collections import defaultdict
n = int(input())

hashmap = defaultdict(int)
for i in range(n):
    a,b = map(int,input().split())
    hashmap[a]+=1
    hashmap[b]-=1

timestamp = sorted(hashmap.keys())

people = 0
ans = 0
for i in timestamp:
    people += hashmap[i]
    ans = max(ans,people)

print(ans)