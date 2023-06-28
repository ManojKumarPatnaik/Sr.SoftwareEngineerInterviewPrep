#This is bottum TLE solution (10^7) is too much for python :(
import sys
mod = (int)(1e9+7)
# map the possible cross section
# ith cross section mapped to (i-1)th cross section
cross = {
    0: [0, 2, 3, 4, 6],
    1: [0, 2, 3, 4, 6],
    2: [0, 2, 3, 4, 6],
    3: [1, 5, 7],
    4: [0, 2, 3, 4, 6],
    5: [1, 5, 7],
    6: [0, 2, 3, 4, 6],
    7: [1, 5, 7]
}

dp = [[0]*8 for _ in range(1000002)]

dp[1] = [1]*8

for i in range(2,1000001):
    for j in range(8):
        for k in cross[j]:
            dp[i][j] +=dp[i-1][k]
        dp[i][j] %=mod

ans = []
for _ in range(int(sys.stdin.readline())):
    h = int(sys.stdin.readline())
    ans.append(str((dp[h][1] + dp[h][5])%mod))

print("\n".join(ans))    
