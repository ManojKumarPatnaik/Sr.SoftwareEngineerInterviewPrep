from collections import deque
n, m = map(int, input().split())

g = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

parent = [-1]*(n+1)
visited = [False]*(n+1)

# bfs
q = deque()
q.appendleft(1)
level = 0
while len(q) > 0:
    for _ in range(len(q)):
        node = q.pop()
        if visited[node]:
            continue
        visited[node] = True
        for child in g[node]:
            q.appendleft(child)
            if parent[child] == -1 and not(visited[child]):
                parent[child] = node
        if node == n:
            q.clear()
            break
    level+=1

p = n
ans = []
while p!=-1:
    ans.append(str(p))
    p = parent[p]
if len(ans) > 1:
    print(level)
    print(" ".join(ans[::-1]))
else:
    print("IMPOSSIBLE")