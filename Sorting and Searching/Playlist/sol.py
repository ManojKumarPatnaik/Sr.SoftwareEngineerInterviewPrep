n = int(input())

a = list(map(int,input().split()))

window = set()

i = 0
j = 0
ans = 1

while j<n:
    window.add(a[j])
    if len(window) ==  (j-i+1):
        ans = max(ans,j-i+1)
        j+=1
    else:
        window.remove(a[i])
        i+=1

print(ans)