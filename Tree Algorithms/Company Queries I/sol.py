from math import *
n, q = map(int, input().split())

d = (int)(log(n, 2))+1

dp = [[0]*(n+1) for _ in range(d)]

dp[0] = [0, 0]+list(map(int, input().split())) #initialization
#filling table
for j in range(1, d):
    for i in range(2, n+1):
        dp[j][i] = dp[j-1][dp[j-1][i]]

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

ans = []
for _ in range(q):
    i, k = map(int, input().split())
    ans.append(kthAncestor(i,k))

print("\n".join(list(map(str,ans))))
