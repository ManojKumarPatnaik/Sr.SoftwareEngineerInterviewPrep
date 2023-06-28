#TLE RECURSIVE SOLUTION
import sys
sys.setrecursionlimit(1000000)
n = int(input())

tree = [[] for i in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

subtree = [0]*(n+1)
distances = [0]*(n+1)


def subtreeSize(node, parent):
    s = 0
    for child in tree[node]:
        if child != parent:
            s += subtreeSize(child, node)
    subtree[node] = s+1
    return s+1


def distanceFrom(node, parent, d):
    distances[node] = d
    for child in tree[node]:
        if child != parent:
            distanceFrom(child, node, d+1)


subtreeSize(1, 1)
distanceFrom(1, 1, 0)

val = sum(distances)

allDistanceSum = [0]*(n+1)
allDistanceSum[1] = val + n


def rerootingTree(node, parent):
    allDistanceSum[node] = allDistanceSum[parent] + n - 2*subtree[node]
    for child in tree[node]:
        if child != parent:
            rerootingTree(child, node)


rerootingTree(1, 1)
print(*allDistanceSum[1:])
