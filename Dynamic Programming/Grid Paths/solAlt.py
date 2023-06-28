import sys
n = int(input())
mod = (int)(1e9+7)

grid = []

for _ in range(n):
    grid.append(sys.stdin.readline().strip())

dp = [[0]*n for _ in range(n)]
dp[n-1][n-1] = 1 if grid[n-1][n-1] =="." else 0 #base condition

for i in range(n-1,-1,-1):
    for j in range(n-1,-1,-1):
        if grid[i][j] == "*":
            continue
        if i+1<n:
            dp[i][j] += dp[i+1][j] #recurrence relation
        if j+1<n:
            dp[i][j] += dp[i][j+1] #recurrence relation
        dp[i][j] %= mod

print(dp[0][0])