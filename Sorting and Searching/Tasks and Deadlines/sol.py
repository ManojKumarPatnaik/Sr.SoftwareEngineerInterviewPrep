n = int(input())
a = [[0,0] for  i in range(n)]

for i in range(n):
    a[i][0],a[i][1] = map(int,input().split())

a.sort(key=lambda x:x[0])

ans = 0
time = 0
for i in a:
    time += i[0]
    ans += i[1] - time
print(ans)