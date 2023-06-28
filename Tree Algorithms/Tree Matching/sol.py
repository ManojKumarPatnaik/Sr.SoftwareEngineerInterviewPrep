#TLE solution
import sys
sys.setrecursionlimit(10**6)
n = int(sys.stdin.readline())

tree = [[] for _ in range(n+1)]

for _ in range(n-1):
    a,b = map(int,sys.stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)

paired = [False]*(n+1)

cnt = 0
def dfs(tree,node,parent):
    for child in tree[node]:
        if child!=parent:
            dfs(tree,child,node)
            if not(paired[node] or paired[child]):
                paired[node] = paired[child] = True
                global cnt
                cnt+=1

dfs(tree,1,1)
print(cnt)