n = int(input())
arr = sorted(list(map(int,input().split())))

height = arr[n//2]
cost = 0
for i in range(n):
    cost += abs(arr[i]-height)

print(cost)

   



