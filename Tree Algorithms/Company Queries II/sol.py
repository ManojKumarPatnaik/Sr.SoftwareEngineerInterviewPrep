from collections import deque
from math import *
import sys
sys.setrecursionlimit(10**6)
n, q = map(int, sys.stdin.readline().split())

d = (int)(log(n, 2))+1

dp = [[0]*(n+1) for _ in range(d)]  # for binary lifting
depth = [-1]*(n+1)  # depth of all nodes
dp[0] = [0, 0]+list(map(int, input().split())) #initialization
#filling table
for j in range(1, d):
    for i in range(2, n+1):
        dp[j][i] = dp[j-1][dp[j-1][i]]

#building actual tree
tree = [[] for _ in range(n+1)]
for i in range(2, n+1):
    tree[dp[0][i]].append(i)

#filling binary lifting table
for j in range(1, d):
    for i in range(1, n+1):
        dp[j][i] = dp[j-1][dp[j-1][i]]


def depthBFS(node, d):
    q = deque()
    q.appendleft(1)
    while len(q) > 0:
        for _ in range(len(q)):
            node = q.pop()
            depth[node] = d
            for child in tree[node]:
                if depth[child] == -1:
                    q.appendleft(child)
        d += 1


def kthAncestor(i,k):
    b = 0
    while k > 0:
        if k & 1:
            i = dp[b][i]
        k >>= 1
        b += 1
    if i == 0:
        i = -1 
    return i


def LCA(u, v):
    if depth[v] > depth[u]:  # u should be lower node
        u, v = v, u
    u = kthAncestor(u, depth[u]-depth[v])  # making u and v at same level

    if u == v:  # if v is already ancestor of u
        return u
    # move both nodes up in bigger steps one by one
    # until their ancesor are not same
    for j in range(d-1, -1, -1):
        if dp[j][u] != dp[j][v]:
            u = dp[j][u]
            v = dp[j][v]
    return dp[0][u]


depthBFS(1, 0)
ans = []
for _ in range(q):
    u, v = map(int, sys.stdin.readline().split())
    ans.append(LCA(u, v))

print("\n".join(list(map(str, ans))))
