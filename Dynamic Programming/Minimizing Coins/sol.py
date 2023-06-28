# TLE in python
import sys
n,x = map(int,sys.stdin.readline().split())
coin =  list(map(int,sys.stdin.readline().split()))

dp=[1e9]*(x+1)
dp[0] = 0

for i in range(1,x+1):
    for c in coin:
        if c<=i:
            dp[i] = min(dp[i],dp[i-c]+1) # recurrence relation
print(dp[x] if dp[x] != 1e9 else -1)