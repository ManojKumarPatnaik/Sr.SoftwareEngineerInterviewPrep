#TLE RECURSIVE SOLUTION
import sys
sys.setrecursionlimit(1000000)
n = int(input())
 
tree = [[] for i in range(n+1)]
 
for _ in range(n-1):
    a,b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)

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
a = dfs(tree,deepNode,-1,height(tree,deepNode,-1))
b = deepNode
#a and b are the ends of diameter


ai = [0]*(n+1) #distance between any node i from a
bi = [0]*(n+1) #distance between any node i from b

def distance(tree,arr,node,parent,d):   
    arr[node] = d
    for child in tree[node]:
        if child != parent:
            distance(tree,arr,child,node,d+1)

distance(tree,ai,a,a,0)
distance(tree,bi,b,b,0)

#final answer
ans = [0]*(n)
for i in range(1,n+1):
    ans[i-1] = max(ai[i],bi[i])
print(" ".join(list(map(str,ans))))
