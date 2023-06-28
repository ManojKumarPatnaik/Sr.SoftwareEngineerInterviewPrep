n,x = map(int,input().split())

a = list(map(int,input().split()))
idx = [i for i in range(n)]

idx.sort(key=lambda x:a[x])

m = {}
for i in range(n):
    for j in range(i+1,n):
        s1 = a[idx[i]]+a[idx[j]]
        if (x-s1) in m.keys():
            print(idx[m[x-s1][0]]+1,idx[m[x-s1][1]]+1,idx[i]+1,idx[j]+1)
            exit(0)
    for k in range(i):
        m[a[idx[i]]+a[idx[k]]] = [k,i]

print("IMPOSSIBLE")