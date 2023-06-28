import sys
sys.setrecursionlimit(1000000)
n = int(input())
mod = (int)(1e9+7)

grid = []

for _ in range(n):
    grid.append(sys.stdin.readline().strip())

memo = [[-1]*n for _ in range(n)]

def fun(i,j):
    if i>=n or j>=n:
        return 0
    if grid[i][j] == "*":
        return 0
    if i == n-1 and j == n-1:
        return 1
    if memo[i][j] != -1:
        return memo[i][j]
    memo[i][j] = (fun(i+1,j)+fun(i,j+1))%mod
    return memo[i][j]

print(fun(0,0))