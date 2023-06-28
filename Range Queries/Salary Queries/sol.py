# TLE solution
n, q = map(int, input().split())

arr = [-1] + list(map(int, input().split()))  # 1 based indexing
coordinates = arr[1:]

queries = [[0]*3 for _ in range(q)]
for i in range(q):
    x, y, z = input().split()
    if x == "!":
        coordinates.append(int(z))
    else:
        coordinates.append(int(y))
        coordinates.append(int(z))
    queries[i][0] = x
    queries[i][1] = int(y)
    queries[i][2] = int(z)

coordinates = sorted(list(set(coordinates))) #only unique salaries required 
n = len(coordinates)
cmp = {}  # compressed coordinates
for i in range(n):  # compressing coordinates
    cmp[coordinates[i]] = i

aa = [0]*(n+1)  # for storing frequency of each salary in compressed index
bit = [0]*(n+1)  # for prefix queries based on aa
for i in arr[1:]:
    aa[cmp[i]] += 1


def update(k, x):  # adds x to kth element
    while k <= n:
        bit[k] += x
        k += (k & -k)


def get(k):  # returns prefix sum till k
    s = 0
    while k >= 1:
        s += bit[k]
        k -= (k & -k)
    return s


# constructing BIT
for i in range(n):
    update(i+1, aa[i])  # 1 based index

#handling queries
for x, y, z in queries:
    if x == "!":
        update(cmp[arr[y]]+1, -1)  # reduce frequency of men with salary arr[y]
        update(cmp[z]+1, +1)  # increase frequency of men with salary z
    else:
        print(get(cmp[z]+1) - get(cmp[y]))
