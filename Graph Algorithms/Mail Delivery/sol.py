import sys
sys.setrecursionlimit(10**6)
from collections import deque
n, m = map(int, input().split())
 
g = [set() for _ in range(n+1)]
degree = [0]*(n+1)
for _ in range(m):
    a, b = map(int, input().split())
    g[a].add(b)
    g[b].add(a)
    degree[a] += 1
    degree[b] += 1
 
flag = True
 
visited = [False]*(n+1)
visited[0] = True
 
def dfs(node):
    stack = deque()
    stack.append(node)
    while len(stack)>0:
        node = stack.pop()
        visited[node]  = True
        for child in g[node]:
            if not(visited[child]):
                stack.append(child)
            

for x in degree: #odd degree check
    if x&1 == 1:
        flag = False
        break
dfs(1)
for i in range(1,n+1): #connected component check
    if degree[i] != 0 and not(visited[i]):
        flag = False
        break
 
def eulerCircuit():
    stack = deque()
    circuit = deque()
    stack.append(1)
    while len(stack)>0:
        node = stack[-1]
        if len(g[node])>0: #unprocessed edges are still present
            child = g[node].pop()
            g[child].remove(node)
            stack.append(child)
        else: #no out edges from current node
            circuit.append(stack.pop())
    return circuit
 
if not(flag):
    print("IMPOSSIBLE")
else:
    print(*eulerCircuit())