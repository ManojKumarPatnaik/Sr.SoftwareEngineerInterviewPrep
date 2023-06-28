n,q = map(int,input().split())

arr = [-1] + list(map(int,input().split()))
bit = [0]*(n+1)

def update(k,x):
    while k<=n:
        bit[k] += x
        k += (k&-k)

def get(k):
    s = 0   
    while k>=1:
        s += bit[k]
        k -= (k&-k)
    return s

for i in range(1,n+1):
    update(i,arr[i])

for _ in range(q):
    o,a,b = map(int,input().split())
    if o == 1:
        update(a,b-arr[a])
        arr[a] = b
    elif o == 2:
        print(get(b) - get(a-1))