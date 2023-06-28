n = int(input())
arr = list(map(int, input().split()))
total = sum(arr)
ans = 1000000000

def rec(arr, i, sack):
    if i < 0:
        return
    global ans
    ans = min(ans, abs((total - sack) - sack))
    rec(arr, i-1, sack+arr[i])
    rec(arr, i-1, sack)


rec(arr, n-1, 0)
print(ans)
