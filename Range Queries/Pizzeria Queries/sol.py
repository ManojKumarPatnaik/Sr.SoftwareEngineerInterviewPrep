import sys
sys.setrecursionlimit(10**6)
INF = (int)(1e9)
n, q = map(int, sys.stdin.readline().split())

p = list(map(int, sys.stdin.readline().split()))


def nextPowerOfN(n):
    p = 1
    while p < n:
        p <<= 1
    return p


n = nextPowerOfN(n)
p += [INF]*(n-len(p))

stLeft = [0]*(2*n)
stRight = [0]*(2*n)


def update(i, x):
    i += n
    stLeft[i] = x-(i-n)
    stRight[i] = x+(i-n)
    i >>= 1
    while i >= 1:
        stLeft[i] = min(stLeft[2*i], stLeft[2*i+1])
        stRight[i] = min(stRight[2*i], stRight[2*i+1])
        i >>= 1


def queryLeft(a, b):
    ans = INF
    a += n
    b += n
    while a < b:
        if a & 1:
            ans = min(ans, stLeft[a])
            a += 1
        if b & 1:
            b -= 1
            ans = min(ans, stLeft[b])
        a >>= 1
        b >>= 1
    return ans


def queryRight(a, b):
    ans = INF
    a += n
    b += n
    while a < b:
        if a & 1:
            ans = min(ans, stRight[a])
            a += 1
        if b & 1:
            b -= 1
            ans = min(ans, stRight[b])
        a >>= 1
        b >>= 1
    return ans


# building trees
for i in range(n):
    update(i, p[i])
# queries
ans = []
for _ in range(q):
    o = list(map(int, sys.stdin.readline().split()))
    if o[0] == 1:
        update(o[1]-1, o[2])
    else:
        ans.append(min(queryLeft(1, o[1])+(o[1]-1),queryRight(o[1], n)-(o[1]-1)))

print("\n".join(list(map(str, ans))))
