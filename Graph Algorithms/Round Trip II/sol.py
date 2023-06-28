import sys
sys.setrecursionlimit(10**6)
n,m = map(int,input().split())

g = [[] for _ in range(n+1)]
parent = [-1]*(n+1)
status=[-1]*(n+1) #0-under process -1-not under process
visited = [False]*(n+1)

for _ in range(m):
    a,b = map(int,input().split())
    g[a].append(b)

last = -1

def dfs(node):
    if visited[node] and status[node] == 0: #found cycle
        global last
        last = node
        return True
    if visited[node]:
        return False
    visited[node] = True
    status[node] = 0 #marking this node 
    res = False
    for child in g[node]:
        parent[child] = node
        res = res or dfs(child)
        if res:
            return True
    status[node] = -1 #unmarking this node 
    return res

for i in range(n):
    if not(visited[i]):
        if dfs(i):
            ans = []
            t = last
            ans.append(t)
            t = parent[t]
            while t!=last:
                ans.append(t)
                t = parent[t]
            ans.append(t)
            print(len(ans))
            print(*ans[::-1])
            exit(0)


print("IMPOSSIBLE")