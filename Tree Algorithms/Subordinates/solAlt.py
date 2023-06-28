import sys
sys.setrecursionlimit(1000000)
n = int(input())

parent = [0,-1]+list(map(int,input().split()))

tree = [set() for i in range(n+1)] 

for i in range(2,n+1):
    tree[parent[i]].add(i)

ans = [1]*(n+1)
def dfs(tree,node):
    for child in tree[node]:
        ans[node] += dfs(tree,child)
    return ans[node]

dfs(tree,1)

for i in range(1,n+1):
    print(ans[i]-1,end=" ")