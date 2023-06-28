n,x = map(int,input().split())

arr = list(map(int,input().split()))
arr.sort()

i = 0
j = n-1
cnt = 0
while i<j:
    if arr[i]+arr[j] <= x:
        i+=1
        j-=1
        cnt+=1
    else:
        j-=1

print(cnt + (n - 2*cnt))