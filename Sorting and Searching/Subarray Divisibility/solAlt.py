n = int(input())
 
a = list(map(int,input().split()))

remainder = [0]*(n)
remainder[0] = 1 # subarray with no elements
sum = 0
for i in range(n):
    sum +=a[i]
    remainder[sum%n]+=1
    
ans = 0
for i in remainder:
    ans += i*(i-1)//2
print(ans)