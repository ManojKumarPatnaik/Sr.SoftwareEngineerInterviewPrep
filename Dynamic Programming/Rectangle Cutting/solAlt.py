#TLE BOTTOM UP
a,b = map(int,input().split())

dp = [[0]*(b+1) for _ in range(a+1)]

for i in range(a+1):
    dp[i][1] = i-1

for j in range(b+1):
    dp[1][j] = j-1

for i in range(a+1):
    for j in range(b+1):
        if i == j:
            dp[i][j] = 0
        else:
            dp[i][j] = i + j -2
            for I in range(1,i):
                dp[i][j] = min(dp[i][j],dp[I][j] + dp[i-I][j]+1)
            for J in range(1,j):
                dp[i][j] = min(dp[i][j],dp[i][J] + dp[i][j-J]+1)
    
print(dp[a][b])
