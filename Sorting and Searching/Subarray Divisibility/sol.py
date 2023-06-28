from collections import defaultdict

n = int(input())
a = list(map(int,input().split()))

prefix = [0]*(n+1)
prefix[1] = a[0]
for i in range(2,n+1):
    prefix[i] = prefix[i-1]+a[i-1]

remainder = [0]*(n+1)
for i in range(n+1):
    remainder[i] = prefix[i]%n

d = defaultdict(int)
ans = 0
for i in range(n+1):
    ans+=d[remainder[i]]
    d[remainder[i]] +=1 

print(ans)
    