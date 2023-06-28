# TLE solution
import sys
n,x = map(int,sys.stdin.readline().split())
coin = list(map(int,sys.stdin.readline().split()))
mod=(int)(1e9+7)
dp=[0]*(x+1)

dp[0] = 1 #base case

for i in range(1,x+1):
    for c in coin:
        if c<=i:
            dp[i] += dp[i-c] # recurrence relation
        dp[i] = dp[i]%mod
print(dp[x])