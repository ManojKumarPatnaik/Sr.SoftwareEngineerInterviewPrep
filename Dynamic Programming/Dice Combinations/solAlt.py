n = int(input())
mod=(int)(1e9+7)
dp=[0]*(n+1)

dp[0] = 1 #base case

for i in range(1,n+1):
    for c in range(1,7):
        if c<=i:
            dp[i] += dp[i-c] # recurrence relation
        dp[i] = dp[i]%mod
print(dp[n])