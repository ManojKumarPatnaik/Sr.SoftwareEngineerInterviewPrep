#TLE RECURSIVE SOLUTION
import sys
sys.setrecursionlimit(1000000)

n = int(input())
mod=(int)(1e9+7)
memo = [-1]*(n+1)

def fun(n):
    if n == 0:
        return 1
    if memo[n]!=-1:
        return memo[n]
    s = 0
    for coin in range(1,7):
        if n>=coin:
            s += fun(n-coin)
    memo[n] = s%mod
    return s%mod

print(fun(n))