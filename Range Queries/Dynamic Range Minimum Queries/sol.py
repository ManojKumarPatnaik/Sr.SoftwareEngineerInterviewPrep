#TLE solution
import sys
sys.setrecursionlimit(10**6)
INF = (int)(1e9)
n, q = map(int, sys.stdin.readline().split())

arr = list(map(int, sys.stdin.readline().split()))


def nextPowerOf2(n):
    p = 1
    if (n and not(n & (n - 1))):
        return n
    while (p < n):
        p <<= 1
    return p


n = nextPowerOf2(n)
arr += [INF]*(n-len(arr))

st = [0]*(2*n)


def update(k, x):
    k += n
    st[k] = x
    k //= 2
    while k >= 1:
        st[k] = min(st[2*k], st[2*k+1])
        k //= 2


def query(qa, qb, a, b, i):
    if qa <= a and b <= qb:
        return st[i]
    if qb < a or qa > b:
        return INF
    mid = a + (b-a)//2
    return min(query(qa, qb, a, mid, 2*i), query(qa, qb, mid+1, b, 2*i+1))


for i in range(n):
    update(i, arr[i])

ans = []
for _ in range(q):
    o, a, b = map(int, sys.stdin.readline().split())
    if o == 1:
        update(a-1, b)
    elif o == 2:
        ans.append(str(query(a, b, 1, n, 1)))

print("\n".join(ans))
