n =  int(input())

arr = list(map(int,input().split()))

ans = min(arr)
sum = 0
for i in range(n):
    sum += arr[i]
    ans = max(sum,ans)
    if sum < 0: # positive subarray ends here
        sum = 0 # starting new subarray

print(ans)
