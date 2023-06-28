import heapq

n,m = map(int,input().split())

g = [[] for _ in range(n+1)]

d = [1e18]*(n+1)
d[1] = 0
pq = [(d[1],1)]
heapq.heapify(pq) 
s = set([1])

for _ in range(m):
    a,b,c = map(int,input().split())
    g[a].append([b,c])

while len(pq)>0:
    node = heapq.heappop(pq)[1]
    s.remove(node)
    for child,wt in g[node]:
        newd = d[node] + wt
        if newd<d[child]:
            d[child] = newd
            if not(child in s):
                heapq.heappush(pq,(d[child],child))
                s.add(child)

print(*d[1:])