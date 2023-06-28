n = int(input())

a = sorted(list(map(int,input().split())))

sum = 1
for i in range(n):
    if a[i] <= sum:
        sum+=a[i]
    else:
        break
print(sum)