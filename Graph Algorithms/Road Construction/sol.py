n,m = map(int,input().split())

parent = [i for i in range(n+1)]
size = [1 for i in range(n+1)]
cnt = n
maxSize= 1

def find(node):
    if node == parent[node]:
        return node
    parent[node] = find(parent[node])
    return parent[node]

def union(a,b):
    if a!=b:
        parent[b] = a
        size[a] += size[b]
        return True
    return False

ans = []
for _ in range(m):
    a,b = map(int,input().split())
    a = find(a)
    b = find(b)
    if union(a,b):
        cnt-=1
        maxSize = max(maxSize,size[a])
    ans.append(str(cnt)+" "+str(maxSize))

print("\n".join(ans))

 

 
