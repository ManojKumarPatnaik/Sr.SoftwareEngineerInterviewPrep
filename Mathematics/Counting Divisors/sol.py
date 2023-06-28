n = 1000001
dp = [0]*(n)

for i in range(1,n):
    for j in range(i,n,i):
        dp[j] += 1

ans = []
for _ in range(int(input())):
    ans.append(dp[int(input())])

print('\n'.join(list(map(str,ans))))