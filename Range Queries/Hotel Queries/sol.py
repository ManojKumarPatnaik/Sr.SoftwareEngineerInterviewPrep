import sys
sys.setrecursionlimit(10**6)
MINF = (int)(-1e9)
n, m = map(int, sys.stdin.readline().split())

arr = list(map(int, sys.stdin.readline().split()))


def nextPowerOf2(n):
    p = 1
    if (n and not(n & (n - 1))):
        return n
    while (p < n):
        p <<= 1
    return p


n = nextPowerOf2(n)
arr += [MINF]*(n-len(arr))

st = [0]*(2*n)


def update(k, x):
    k += n
    st[k] = x
    k //= 2
    while k >= 1:
        st[k] = max(st[2*k], st[2*k+1])
        k //= 2


def query(i,x):
    if st[i]<x:
        return -1
    if i>=n and st[i]>=x:
        return i-n 
    if 2*i<2*n and st[2*i]>=x:
        return query(2*i,x)
    if 2*i+1<2*n:
        return query(2*i+1,x)
    return -1


for i in range(n):
    update(i, arr[i])

r = list(map(int,input().split()))
ans = []
for x in r:
    idx = query(1,x)
    ans.append(str(idx+1))
    update(idx,arr[idx]-x)
    arr[idx] -= x

print(" ".join(ans))
