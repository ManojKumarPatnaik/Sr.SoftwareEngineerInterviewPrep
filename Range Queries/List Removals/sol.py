import sys
sys.setrecursionlimit(10**6)
n = int(input())

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

st = [0]*(2*n)

def update(k):
    k += n
    st[k] = 1 if arr[k-n]!=0 else 0
    k //= 2
    while k >= 1:
        st[k] = st[2*k]+st[2*k+1]
        k //= 2


def query(i,x):
    st[i] -=1
    if i>=n:
        return i-n 
    if 2*i<2*n and st[2*i]>=x:
        return query(2*i,x)
    if 2*i+1<2*n:
        return query(2*i+1,x-st[2*i])
    return -1


for i in range(n):
    update(i)

q = list(map(int,input().split()))
ans = []
for x in q:
    idx = query(1,x)
    ans.append(str(arr[idx]))

print(" ".join(ans))
