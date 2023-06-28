#TLE solution
import sys
sys.setrecursionlimit(1000000)
n,x = map(int,input().split())

w = list(map(int,input().split()))
v = list(map(int,input().split()))

memo =[{} for _ in range(n)]

def fun(i,wt):
    if wt<0:
        return -1e9
    if i == -1:
        return 0
    if wt in memo[i].keys():
        return memo[i][wt]
    memo[i][wt] = max(fun(i-1,wt),fun(i-1,wt-w[i])+v[i])
    return memo[i][wt]

print(fun(n-1,x))