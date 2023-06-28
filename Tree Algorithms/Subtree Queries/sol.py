#TLE RECURSIVE SOLUTION
import sys
sys.setrecursionlimit(10**6)
n,q = map(int,sys.stdin.readline().split())

tree = [[] for _ in range(n+1)]
val = [0]+list(map(int,sys.stdin.readline().split())) #value of each node
subtreeSize = [1]*(n+1)

for _ in range(n-1):
    a,b = map(int,sys.stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)

#creating flat tree
nodeId = []
nodeValue = []
def flat(node,parent):
    nodeId.append(node)
    nodeValue.append(val[node])
    for child in tree[node]:
        if child != parent:
            flat(child,node)

def subtree(node,parent):
    for child in tree[node]:
        if child != parent:
            subtreeSize[node] += subtree(child,node)
    return subtreeSize[node]

flat(1,1)
subtree(1,1)

#making sum segment tree
def nextPowerOf2(n):
    p = 1
    while p<n:
        p<<=1
    return p
n = nextPowerOf2(n)
nodeId += [0]*(n-len(nodeId))
nodeValue += [0]*(n-len(nodeValue))

st = [0]*(2*n)

def update(i,x):
    i+=n
    st[i] = x
    i>>=1
    while i>=1:
        st[i] = st[2*i]+st[2*i+1]
        i>>=1

#return sum between [a+1,b]
def query(a,b):
    ans = 0
    a+=n
    b+=n
    while a<b:
        if a&1:
            ans +=st[a]
            a+=1
        if b&1:
            b-=1
            ans += st[b]
        a>>=1
        b>>=1
    return ans 

for i in range(n):
    update(i,nodeValue[i])

#which node at what index in st?
ii = [0]*(n+1)
for i in range(n):
    ii[nodeId[i]] = i+1
#queries
ans = []
for _ in range(q):
    o = list(map(int,sys.stdin.readline().split()))
    if o[0] == 1:
        update(ii[o[1]]-1,o[2])
    else:
        idx = ii[o[1]]
        ans.append(query(idx-1,idx+subtreeSize[o[1]]-1))

print("\n".join(list(map(str,ans))))