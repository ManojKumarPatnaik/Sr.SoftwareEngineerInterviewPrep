n, m, k = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort()

ans = 0

x = 0  # for requirement apartment size
y = 0  # for available apartment size

while x < len(a) and y < len(b):
    # condition for match
    if abs(a[x]-b[y]) <= k:
        x += 1
        y += 1
        ans += 1
    elif a[x]+k < b[y]:
        # condition for no match for this applicant
        x += 1
    else:
        # condition when this appartment can't be alloted to any applicant
        y += 1

print(ans)
