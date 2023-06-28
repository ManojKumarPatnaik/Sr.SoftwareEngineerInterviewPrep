n = int(input())

arr = list(map(int,input().split()))
a = [0]*(n+1)
for i in range(n):
    a[arr[i]] = i

ans = 1 #at least one round to pick all numbers
for i in range(1,n+1):
    if a[i-1] > a[i]:
        ans+=1
print(ans)