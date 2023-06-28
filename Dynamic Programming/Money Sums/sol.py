#RECURSIVE SOLUTION
import sys
sys.setrecursionlimit(100000)
n = int(input())

x = list(map(int,input().split()))

res = [False]*(100001)
memo = [[False]*(100001) for _ in range(101)]

def fun(i,s):
    res[s] = True
    if i == n:
        return
    if memo[i][s]:
        return 
    fun(i+1,s)
    fun(i+1,s+x[i])
    memo[i][s] = True 

fun(0,0)
ans = []
for i in range(1,100001):
    if res[i]:
        ans.append(str(i))
print(len(ans))
print(" ".join(ans))
    