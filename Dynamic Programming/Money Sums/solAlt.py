#ITERATIVE SOLUTION
n = int(input())

x = list(map(int,input().split()))

res = [False]*(100001)
res[0] = True

for a in x:
    for i in range(100000,-1,-1):
        if res[i]:
            res[i+a] = True

ans = []
for i in range(1,100001):
    if res[i]:
        ans.append(str(i))
print(len(ans))
print(" ".join(ans))