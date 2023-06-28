#TLE RECURSIVE
import sys
sys.setrecursionlimit(10**6)
a,b = map(int,input().split())

memo = [[-1]*(b+1) for _ in range(a+1)]

def fun(i,j):
    if i == j:
        return 0
    if i == 1:
        return j-1
    if j == 1:
        return i-1
    if memo[i][j] != -1:
        return memo[i][j]

    memo[i][j] = i + j -2
    for I in range(1,i):
        memo[i][j] = min(memo[i][j],fun(I,j) + fun(i-I,j)+1)
    for J in range(1,j):
        memo[i][j] = min(memo[i][j],fun(i,J) + fun(i,j-J)+1)
    return memo[i][j]

print(fun(a,b))