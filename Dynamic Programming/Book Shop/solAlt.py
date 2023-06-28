# TLE solution
import sys
n, x = map(int, sys.stdin.readline().split())

w = [0]+list(map(int, sys.stdin.readline().split()))
v = [0]+list(map(int, sys.stdin.readline().split()))


dp = [[0]*(x+1) for _ in range(2)]

for i in range(1, n+1):
    for j in range(x+1):
        dp[1][j] = max(dp[0][j], (dp[0][j-w[i]] + v[i]) if (j-w[i] >= 0) else 0)
    dp[0] = dp[1]
    dp[1] = [0]*(x+1)

print(dp[0][x])
