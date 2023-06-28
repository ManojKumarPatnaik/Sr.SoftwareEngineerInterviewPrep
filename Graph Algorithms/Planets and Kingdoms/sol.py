from collections import deque
import sys
sys.setrecursionlimit(10**6)
n, m = map(int, input().split())

g = [[] for _ in range(n+1)]
grev = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    grev[b].append(a)

visited = [False]*(n+1)
stack = deque()


def dfs1(graph, node):
    visited[node] = True
    for child in graph[node]:
        if not(visited[child]):
            dfs1(graph, child)
    stack.append(node)


for i in range(1, n+1):
    if not(visited[i]):
        dfs1(g, i)

visited = [False]*(n+1)
visited[0] = -1
label = [0]*(n+1)
l = 1


def dfs2(graph, node):
    visited[node] = True
    label[node] = l
    for child in graph[node]:
        if not(visited[child]):
            dfs2(graph, child)


while len(stack) > 0:
    node = stack.pop()
    if not(visited[node]):
        dfs2(grev, node)
        l += 1

print(max(label))
print(*label[1:])
