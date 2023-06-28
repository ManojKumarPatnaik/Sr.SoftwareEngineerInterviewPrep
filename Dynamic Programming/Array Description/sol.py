#TLE recursive solution
import sys
sys.setrecursionlimit(1000000)
mod = (int)(1e9+7)
n, m = map(int, input().split())

x = list(map(int, sys.stdin.readline().split()))

memo = [[-1]*(m+1) for _ in range(n+1)]

def fun(x, i, prev):
    if i == n:
        return 1
    elif memo[i][prev] != -1:
        return memo[i][prev]
    elif x[i] == 0:
        s = 0
        for k in range(1, m+1):
            if prev == -1 or abs(k-prev) <= 1:
                s += fun(x, i+1, k)
        memo[i][prev] = s % mod
    elif prev == -1 or abs(prev - x[i]) <= 1:
        memo[i][prev] = fun(x, i+1, x[i])
    else:
        memo[i][prev] = 0
    return memo[i][prev]


print(fun(x, 0, -1))
