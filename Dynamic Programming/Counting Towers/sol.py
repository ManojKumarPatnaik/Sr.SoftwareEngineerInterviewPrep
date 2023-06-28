# This solution work only for values <1000. since going higher makes python to fail
# But logically this is correct answer
import sys
sys.setrecursionlimit(1000000)
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

memo = [[-1]*8 for _ in range(1000001)]

def fun(n,c):
    if n ==1:
        return 1
    if memo[n][c]!=-1:
        return memo[n][c]
    s = 0
    for next in cross[c]:
        s += fun(n-1,next)%mod
    memo[n][c] = s%mod
    return memo[n][c]

fun(1000,1) 
fun(1000,5)

for _ in range(int(input())):
    h = int(input())
    print(memo[h][1] + memo[h][5])    
