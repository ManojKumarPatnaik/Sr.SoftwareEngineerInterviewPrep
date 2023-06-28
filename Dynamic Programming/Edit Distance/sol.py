import sys
sys.setrecursionlimit(10**6)
A = "X"+input()
B = "X"+input()

memo = [[-1]*(len(B)) for _ in range(len(A))]

def fun(i,j):
    if i == 0:
        return j
    if j == 0:
        return i
    if memo[i][j] !=-1:
        return memo[i][j]
    if A[i] == B[j]:
        memo[i][j] = fun(i-1,j-1)
    else:
        memo[i][j] = min(fun(i-1,j),fun(i-1,j-1),fun(i,j-1)) + 1
    return memo[i][j]
     
print(fun(len(A)-1,len(B)-1))