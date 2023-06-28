n = int(input())

x = list(map(int,input().split()))

dp = [[0]*(n+1) for _ in range(n+1)]

for i in range(n-1,-1,-1):
    for j in range(i,n):
        if i == j:
            dp[i][i] = x[i]
        else:
            dp[i][j] = max(x[i] - dp[i+1][j],x[j] - dp[i][j-1])

print((dp[0][n-1]+sum(x))//2)