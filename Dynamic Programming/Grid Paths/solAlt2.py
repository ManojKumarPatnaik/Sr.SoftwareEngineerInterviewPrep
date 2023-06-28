import sys
n = int(input())
mod = (int)(1e9+7)

grid = []

for _ in range(n):
    grid.append(sys.stdin.readline().strip())

dp = [[0]*n for _ in range(2)]
dp[0][n-1] = 1 if grid[n-1][n-1] =="." else 0 #base condition

for i in range(n-1,-1,-1):
    for j in range(n-1,-1,-1):
        if grid[i][j] == "*":
            dp[0][j] = 0
            continue
        if i+1<n:
            dp[0][j] += dp[1][j] #recurrence relation
        if j+1<n:
            dp[0][j] += dp[0][j+1] #recurrence relation
        dp[0][j] %= mod
    dp[1] = dp[0]
    dp[0] = [0]*(n)
    
print(dp[1][0])