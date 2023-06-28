n = int(input())

dp = [1e9]*(n+1)
for i in range(min(10,n+1)):
    dp[i] = 1

for i in range(10,n+1):
    t = i
    while t>0:
        d = t%10
        t //= 10
        dp[i] = min(dp[i],dp[i-d]+1)

print(dp[n])