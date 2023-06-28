#TLE Solution 4 test cases
import sys
sys.setrecursionlimit(10**6)
n, m = map(int, sys.stdin.readline().split())

g = [[] for _ in range(n+1)]
predecessor = [-1]*(n+1)

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    g[a].append([b, c])

for i in range(1,n+1): # for connecting dummy node
    g[0].append([i,0])

d = [1e18]*(n+1)
d[0] = 0 # setting up dummy node as source

lastRelaxed = None
def relax():
    res = False
    for node in range(n+1):
        for child, wt in g[node]:
            newd = d[node]+wt
            if newd < d[child]:
                d[child] = newd
                predecessor[child] = node
                global lastRelaxed
                lastRelaxed = child
                res = True
    return res



for _ in range(n-1):
    relax()

if relax():
    for _ in range(n-1): # for entering the cycle
        lastRelaxed = predecessor[lastRelaxed]
    t = lastRelaxed
    ans = [str(lastRelaxed)]
    lastRelaxed = predecessor[lastRelaxed]
    while lastRelaxed!=t:
        ans.append(str(lastRelaxed))
        lastRelaxed = predecessor[lastRelaxed]
    ans.append(str(lastRelaxed))
    print("YES")
    print(" ".join(ans[::-1]))
else:
    print("NO")
