#TLE Recursive solution
import sys
sys.setrecursionlimit(100000)
n = int(input())

x = list(map(int,input().split()))

memo = [[-1]*(n+1) for _ in range(n+1)]

def fun(i,j):
    if i>j:
        return 0
    if i == j:
        return x[i]
    if memo[i][j]!=-1:
        return memo[i][j]
    memo[i][j] = max( x[i]-fun(i+1,j) , x[j]-fun(i,j-1) )
    return memo[i][j]

print((fun(0,n-1)+sum(x))//2)