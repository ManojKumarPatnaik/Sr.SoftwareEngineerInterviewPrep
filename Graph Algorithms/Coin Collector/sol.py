# TLE solution
from collections import deque
import sys
sys.setrecursionlimit(10**6)
n, m = map(int, input().split())

nodeCost = [0] + list(map(int, input().split()))
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

newN = l-1
dag = [[] for _ in range(newN+1)]
ssrCost = [0]*(newN+1)
for i in range(1, n+1):
    ssrCost[label[i]] += nodeCost[i]

for i in range(1, n+1):
    for j in g[i]:
        if label[i] != label[j]:
            dag[label[i]].append(label[j])

visited = [False]*(newN+1)


def dfs3(node):
    if visited[node]:
        return ssrCost[node]
    maxi = 0
    for child in dag[node]:
        if not(visited[child]):
            dfs3(child)
        maxi = max(maxi, ssrCost[child])
    ssrCost[node] += maxi
    visited[node] = True
    return ssrCost[node]


for i in range(1, newN+1):
    if not(visited[i]):
        dfs3(i)

print(max(ssrCost))
