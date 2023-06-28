#TLE solution
n,m = map(int,input().split())
 
E = []
for _ in range(m):
    a,b,c = map(int,input().split())
    E.append([a,b,c])
 
E.sort(key=lambda x:x[2])
parent = [i for i in range(n+1)]
 
def find(node):
    if node == parent[node]:
        return node
    parent[node] = find(parent[node])
    return parent[node]
 
def union(a,b):
    A = find(a)
    B = find(b)
    if A!=B:
        parent[B] = A
        return True
    return False
 
cnt = 0
ans = 0
for a,b,c in E:
    if union(a,b):
        cnt+=1
        ans+=c
    if cnt == n-1:
        break
if cnt == n-1:
    print(ans)
else:
    print("IMPOSSIBLE")