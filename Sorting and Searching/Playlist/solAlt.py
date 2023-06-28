n = int(input())

a = list(map(int,input().split()))

id = [i for i in range(n)]

id.sort(key=lambda x:a[x])

leftNeighbour = [-1]*n

for i in range(1,n):
    if a[id[i]] == a[id[i-1]]:
        leftNeighbour[id[i]] = id[i-1]

ans = 0
nearestNeighbour = -1
for i in range(n):
    if leftNeighbour[i] != -1:
        nearestNeighbour = max(nearestNeighbour,leftNeighbour[i])
    ans = max(ans,i-nearestNeighbour)

print(ans)