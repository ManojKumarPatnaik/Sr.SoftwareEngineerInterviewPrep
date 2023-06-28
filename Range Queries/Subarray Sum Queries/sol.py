import sys
n, m = map(int, sys.stdin.readline().split())

arr = list(map(int, sys.stdin.readline().split()))


def nextPowerOfN(n):
    p = 1
    while p < n:
        p <<= 1
    return p


n = nextPowerOfN(n)
arr += [0]*(n-len(arr))

st = [0]*(2*n)  # main st which store maximum subarray sum
stprefix = [0]*(2*n)  # st to store max prefix sum
stsuffix = [0]*(2*n)  # st to store max suffix sum
stsum = [0]*(2*n)  # st to store sum of range


def update(i, x):
    i += n
    st[i] = x
    stprefix[i] = max(0, x)
    stsuffix[i] = max(0, x)
    stsum[i] = x
    i >>= 1
    while i >= 1:
        stsum[i] = stsum[2*i]+stsum[2*i+1]
        stprefix[i] = max(stprefix[2*i], stsum[2*i]+stprefix[2*i+1])
        stsuffix[i] = max(stsuffix[2*i+1], stsum[2*i+1]+stsuffix[2*i])
        st[i] = max(st[2*i], st[2*i+1], stsuffix[2*i]+stprefix[2*i+1])
        i >>= 1


for i in range(n):
    update(i, arr[i])

ans = []
for _ in range(m):
    k, x = map(int, sys.stdin.readline().split())
    update(k-1, x)
    ans.append(st[1])

print("\n".join(list(map(str, ans))))
