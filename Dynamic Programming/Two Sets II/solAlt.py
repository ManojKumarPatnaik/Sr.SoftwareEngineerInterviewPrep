n = int(input())

if (n*(n+1)/2)%2 !=0:
    print(0)
    exit(0)

mod = (int)(1e9+7)
res = n*(n+1)//4

dp = [[0]*(res+1) for _ in range(n+2)]


dp[n+1][0] = 1
for i in range(n,0,-1):
    for j in range(1,res+1):
            dp[i][j] = (dp[i+1][j] + dp[i+1][j-i])%mod

print(dp[1][res])