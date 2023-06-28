#TLE RECURSIVE SOLUTION
import sys
sys.setrecursionlimit(10**6)
n = int(input())

tree = [[] for _ in range(n+1)]

for _ in range(n-1):
    a,b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)

subtreeSize = [1]*(n+1)

def subtree(node,parent):
    for child in tree[node]:
        if child != parent:
            subtreeSize[node] += subtree(child,node)
    return subtreeSize[node]

subtree(1,1)

def centroid(node,parent):
    flag = True
    for child in tree[node]:
        if child != parent and subtreeSize[child] > n//2:
            flag = False
            centroid(child,node)
    if flag:
        print(node)

centroid(1,1)