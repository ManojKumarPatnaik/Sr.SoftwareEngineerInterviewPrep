import sys
mod = (int)(1e9+7)
n, m = map(int, input().split())

x = list(map(int, sys.stdin.readline().split()))

dp = [[0]*(m+1) for _ in range(n+1)]
dp[n] = [0]+[1]*(m)

for i in range(n-1,0,-1):
    for j in range(1,m+1):
        if x[i] == 0:
            for k in range(j-1, j+2):
                if k<=m:
                    dp[i][j] = (dp[i][j]+dp[i+1][k])%mod
        elif abs(x[i]-j)<=1:
            dp[i][j] = dp[i+1][x[i]]
        else:
            dp[i][j] = 0

if x[0] == 0:
    print(sum(dp[1])%mod)
else:    
    print(dp[1][x[0]])