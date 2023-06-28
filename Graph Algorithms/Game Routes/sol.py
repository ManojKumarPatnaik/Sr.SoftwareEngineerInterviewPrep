import sys
sys.setrecursionlimit(10**6)
mod = (int)(1e9+7)
n,m = map(int,input().split())

g = [[] for _ in range(n+1)]

c = [-1]*(n+1)

for _ in range(m):
    a,b = map(int,input().split())
    g[a].append(b)

def dfs(node):
    if node == n:
        return 1
    if c[node] !=-1:
        return c[node]
    cnt = 0
    for child in g[node]:
        cnt += dfs(child)
    c[node] = cnt%mod
    return c[node]

dfs(1)
print(c[1])