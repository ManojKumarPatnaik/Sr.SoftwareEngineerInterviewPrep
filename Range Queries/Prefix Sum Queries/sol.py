#TLE solution
import sys
sys.setrecursionlimit(10**6)
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
arr += [0]*(n-len(arr))

st = [0]*(2*n)  # to store range sum
stpref = [0]*(2*n)  # to store range max prefix sum


def update(k, x):
    k += n
    st[k] = x
    stpref[k] = x
    k //= 2
    while k >= 1:
        st[k] = st[2*k]+st[2*k+1]
        stpref[k] = max(stpref[2*k], st[2*k] + stpref[2*k+1])
        k //= 2

# each query returns an array of two numbers
# first element is the sum of range a,b
# the second element is the max prefix sum of range a,b
def queryPrefix(qa, qb, a, b, i):
    if qa <= a and b <= qb: #totally in range
        return [st[i],max(0,stpref[i])] 
    if qb < a or qa > b: #totally out range
        return [0,0]
    mid = a + (b-a)//2
    left = queryPrefix(qa, qb, a, mid, 2*i)
    right = queryPrefix(qa, qb, mid+1, b, 2*i+1)
    return [left[0]+right[0] , max(left[1],left[0]+right[1])]

#building ST
for i in range(n):
    update(i, arr[i])
ans = []
for _ in range(q):
    o, a, b = map(int, sys.stdin.readline().split())
    if o == 1:
        update(a-1, b)
    elif o == 2:
        ans.append(str(queryPrefix(a, b, 1, n, 1)[1]))

print("\n".join(ans))
