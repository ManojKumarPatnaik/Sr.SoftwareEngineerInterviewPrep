from collections import deque
n, m = map(int, input().split())

g = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

visited = [False]*(n+1)
color = [-1]*(n+1)

def bfs(node,c):
    q = deque()
    q.appendleft(node)
    while len(q)>0:
        for _ in range(len(q)):
            node = q.pop()
            if visited[node]:
                continue
            visited[node] = True
            color[node] = c
            for child in g[node]:
                if color[child] == color[node]:
                    return False
                if visited[child]:
                    continue
                q.appendleft(child)
        c = 1-c
    return True

bi = True
for i in range(n):
    if not(visited[i]):
        bi = bi and bfs(i,0)

if(bi):
    print(*[i+1 for i in color][1:])
else:
    print("IMPOSSIBLE")