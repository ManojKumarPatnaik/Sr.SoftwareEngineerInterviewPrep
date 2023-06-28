n,x = map(int,input().split())

a = list(map(int,input().split()))

i = j = sum = ans = 0
while j<n or i<n:
    if sum == x:
        ans+=1
    if j<n and sum<x:
        sum+=a[j]
        j+=1
    elif i<n:
        sum-=a[i]
        i+=1
print(ans)