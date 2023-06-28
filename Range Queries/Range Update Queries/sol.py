n,q = map(int,input().split())

arr = [0] + list(map(int,input().split()))
diff = [0]*(n+1)

for i in range(1,n+1):
    diff[i] = arr[i] - arr[i-1]

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
    update(i,diff[i])

for _ in range(q):
    o = list(map(int,input().split()))
    if o[0] == 1:
        a = o[1]
        b = o[2]
        u = o[3]
        update(a,u)
        update(b+1,-u)
    else:
        k = o[1]
        print(get(k))