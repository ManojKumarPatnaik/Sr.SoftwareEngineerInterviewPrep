import sys
sys.setrecursionlimit(10**6)
n, m = map(int, sys.stdin.readline().split())

g = [[] for _ in range(n+1)]
grev = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    g[a].append([b, c*-1])
    grev[b].append(a)

d = [1e18]*(n+1)
d[1] = 0

valid = [False]*(n+1)
def dfs(node):
    if valid[node]:
        return 
    valid[node] = True
    for child in grev[node]:
        dfs(child)


def relax():
    res = False
    for node in range(1, n+1):
        for child, wt in g[node]:
            if valid[node] and valid[child]:
                newd = d[node]+wt
                if newd < d[child]:
                    d[child] = newd
                    res = True
    return res


dfs(n) #to consider only valid nodes

for _ in range(n-1):
    relax()
print(d)
print(valid)
if relax():
    print(-1)
else:
    print(-1*d[-1])
