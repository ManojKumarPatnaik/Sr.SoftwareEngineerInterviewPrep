#TLE recursive solution
import sys
sys.setrecursionlimit(10**6)
n,m = map(int,sys.stdin.readline().split())
g = []
for _ in range(n):
    g.append(sys.stdin.readline())

iland = [[-1]*m for _ in range(n)]

def fun(i,j):
    if not(i>=0 and i<n and j>=0 and j<m):
        return 
    if g[i][j] != "." or iland[i][j] == 1:
        return 
    iland[i][j] = 1
    fun(i+1,j)
    fun(i-1,j)
    fun(i,j+1)
    fun(i,j-1)

cnt = 0
for i in range(n):
    for j in range(m):
        if g[i][j] == "." and iland[i][j] == -1 :
            fun(i,j)
            cnt+=1
        
print(cnt) 