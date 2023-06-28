#TLE RECURSIVE SOLUTION
import sys
sys.setrecursionlimit(100000)
n = int(input())

if (n*(n+1)/2)%2 !=0:
    print(0)
    exit(0)

mod = (int)(1e9+7)
res = n*(n+1)//4

memo = [[-1]*(res+1) for _ in range(n+1)]

def fun(i,s):
    if i > n or s>res:
        return 0
    if s == 0:
        return 1
    if memo[i][s]!=-1:
        return memo[i][s]
    memo[i][s]  = (fun(i+1,s) + fun(i+1,s-i))%mod
    return memo[i][s]

print(fun(1,res))