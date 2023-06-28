# accepted in pypy3
from sys import stdin

n, k = map(int, stdin.readline().split())

a = list(map(int, stdin.readline().strip().split()))

def check(a, maxsum, k):
    subcount = 1
    runsum = 0
    for i in range(n):
        if runsum + a[i] <= maxsum:
            runsum += a[i]
        else:
            runsum = a[i]
            subcount += 1
        if subcount > k:
            return False
    return True


i = max(a)
j = sum(a)

ans = 1e18
while i <= j:
    mid = i + (j-i)//2
    if check(a, mid, k):
        ans = min(ans, mid)
        j = mid-1
    else:
        i = mid+1

print(ans)