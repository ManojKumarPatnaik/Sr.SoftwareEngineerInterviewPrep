n,m = map(int,input().split())

sets = [-1]*(n+1)

def head(i):
    if sets[i] ==-1:
        return i
    sets[i] = head(sets[i])
    return sets[i]

def union(i,j):
    pi = head(i)
    pj = head(j)
    if pi != pj:
        sets[pj] = pi

for _ in range(m):
    a,b = map(int,input().split())
    union(a,b)

heads = [i for i in range(1,n+1) if sets[i] == -1]

print(len(heads)-1)
for i in range(1,len(heads)):
    print(heads[i-1],heads[i])
