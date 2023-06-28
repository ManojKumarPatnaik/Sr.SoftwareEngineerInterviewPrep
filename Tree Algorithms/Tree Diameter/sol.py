# TLE recursive version
import sys
sys.setrecursionlimit(1000000)
n = int(input())
 
tree = [set() for i in range(n+1)]
 
for _ in range(n-1):
    a,b = map(int,input().split())
    tree[a].add(b)
    tree[b].add(a)
 
ans = 0
def dfs(tree,node,parent):
    h1 = h2 = 0
    for child in tree[node]:
        if child != parent:
            hsub = dfs(tree,child,node)
            if hsub > h1:
                h2 = h1
                h1 = hsub
            elif hsub > h2:
                h2 = hsub
    global ans
    ans = max(ans,h1+h2)
    return h1+1
 
dfs(tree,1,1)
 
print(ans)