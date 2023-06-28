#TLE recursive solution
import sys
sys.setrecursionlimit(10**6)
n, m = map(int, input().split())

g = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

visited = [False]*(n+1)
color = [-1]*(n+1)

def dfs(node,c):
    if visited[node]:
        return True
    visited[node] = True
    color[node] = c
    res = True
    for child in g[node]:
        if color[child] == color[node]:
            return False
        res = res and dfs(child,1-c)
    return res

bi = True
for i in range(n):
    if not(visited[i]):
        bi = bi and dfs(i,0)

if(bi):
    print(*[i+1 for i in color][1:])
else:
    print("IMPOSSIBLE")