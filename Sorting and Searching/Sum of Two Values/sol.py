n,x = map(int,input().split())

arr = [[0,0] for _ in range(n)]
a = list(map(int,input().split()))

for i in range(n):
    arr[i][0] = a[i]
    arr[i][1] = i

arr.sort(key=lambda x:x[0])

i = 0
j = n-1

while i<j:
    if arr[i][0]+arr[j][0] == x:
        break
    elif arr[i][0]+arr[j][0]>x:
        j-=1
    else:
        i+=1

if i == j:
    print("IMPOSSIBLE")
else:
    print(arr[i][1]+1,arr[j][1]+1)