# TLE recursive version
import sys
sys.setrecursionlimit(1000000)
n = int(input())
 
tree = [set() for i in range(n+1)]
 
for _ in range(n-1):
    a,b = map(int,input().split())
    tree[a].add(b)
    tree[b].add(a)

def height(tree,node,parent):
    h = -1
    for child in tree[node]:
        if child!=parent:
            h = max(h,height(tree,child,node))
    return h+1
 
def dfs(tree,node,parent,h):
    if(h == 0):
        return node
    for child in tree[node]:
        if child != parent:
            res = dfs(tree,child,node,h-1)
            if res != None:
                return res

# making 1 node as root
h = height(tree,1,-1)
# finding the deepest node
deepNode = dfs(tree,1,-1,h)
# making deepest node as root
print(height(tree,deepNode,-1))