from collections import deque
n, m = map(int, input().split())

g = [[] for _ in range(n+1)]
inedges = [0]*(n+1)
for _ in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    inedges[b] += 1

q = deque()
for i in range(1, n+1):  # collect all sinks
    if inedges[i] == 0:
        q.appendleft(i)

topo = []
while len(q) > 0:
    for _ in range(len(q)):
        node = q.pop()
        topo.append(node)
        for child in g[node]:
            inedges[child] -= 1  # disconnect edge
            if inedges[child] == 0:  # add newly created sinks
                q.appendleft(child)

if sum(inedges) != 0:
    print("IMPOSSIBLE")
else:
    print(*topo)
