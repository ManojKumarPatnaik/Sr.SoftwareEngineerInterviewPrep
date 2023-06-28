from collections import defaultdict

n,x = map(int,input().split())
a = list(map(int,input().split()))

prefix = [0]*(n+1)
prefix[1] = a[0]
for i in range(2,n+1):
    prefix[i] = prefix[i-1]+a[i-1]

d = defaultdict(int)
ans = 0
for i in range(n+1):
    ans+=d[prefix[i]-x]
    d[prefix[i]] +=1 

print(ans)
    