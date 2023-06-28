import sys
n,m,q = map(int,sys.stdin.readline().split())

g = [[1e18]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a,b,c = map(int,sys.stdin.readline().split())
    g[a][b] = min(g[a][b],c)
    g[b][a] = min(g[b][a],c)

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            g[i][j] = min(g[i][j] , g[i][k] + g[k][j])

ans = []
for _ in range(q):
    a,b = map(int,sys.stdin.readline().split())
    if g[a][b] == 1e18:
        ans.append("-1")
    else:
        ans.append(str(g[a][b]))

print("\n".join(ans))