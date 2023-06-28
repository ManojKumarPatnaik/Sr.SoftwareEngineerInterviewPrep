import sys
sys.setrecursionlimit(10**6)
n,m = map(int,input().split())

g = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    g[a].append(b)
    g[b].append(a)

ans = []
visited = [False]*(n+1)
def dfs(node,parent):
    if visited[node]: #cycle detection
        ans.append(node)
        return True
    visited[node] = True
    for child in g[node]:
        if child == parent:
            continue
        if dfs(child,node):
            ans.append(node)
            return True
    return False
    
for i in range(1,n+1):
    if not(visited[i]):
        if dfs(i,-1):
            cycleEnd = ans[1:].index(ans[0])
            print(cycleEnd+2)
            print(*ans[:cycleEnd+2])
            exit(0)

print("IMPOSSIBLE")
