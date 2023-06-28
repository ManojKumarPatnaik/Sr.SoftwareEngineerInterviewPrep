from collections import deque
n = int(input())

parent = [0,-1]+list(map(int,input().split()))

directChildrenCnt = [0]*(n+1)
for i in range(2,n+1):
    directChildrenCnt[parent[i]]+=1

leaf = deque()
for i in range(1,n+1):
    if directChildrenCnt[i] == 0:
        leaf.appendleft(i)
    
ans = [1]*(n+1)
while len(leaf)>0:
    node = leaf.pop()
    if parent[node]!=-1:
        ans[parent[node]] +=ans[node] # add subtree size to size of parent
        directChildrenCnt[parent[node]] -=1 #remove current node logically from tree
        if directChildrenCnt[parent[node]] == 0: #add new leaf node
            leaf.appendleft(parent[node])
    
for i in range(1,n+1):
    print(ans[i]-1,end=" ")