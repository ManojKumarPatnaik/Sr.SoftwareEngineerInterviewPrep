#TLE solution on 3 test cases
import sys
sys.setrecursionlimit(10**6)
from collections import deque
n,m = map(int,input().split())

g = [[] for _ in range(n+1)]
grev = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    g[a].append(b)
    grev[b].append(a)

visited = [False]*(n+1)
stack = deque() #to store order in which nodes are processed
def dfs1(graph,node):
    visited[node] = True
    for child in graph[node]:
        if not(visited[child]):
            dfs1(graph,child)
    stack.append(node)

for i in range(1,n+1):
    if not(visited[i]):
        dfs1(g,i)

visited = [False]*(n+1)
visited[0] = -1

def dfs2(graph,node): #simple dfs
    visited[node] = True
    for child in graph[node]:
        if not(visited[child]):
            dfs2(graph,child)

dfs2(grev,stack[-1])
if visited.count(True) != n:
    print("NO")
    print(visited.index(False),visited.index(True))
else:
    print("YES")