n,t = map(int,input().split())
k = list(map(int,input().split()))

def check(k,time,target):
    temp = 0
    for i in range(n):
        temp += time//k[i]
        if temp>=target:
            return True
    return False


i = 0
j = max(k)*t
ans = j
while i<=j:
    mid = i+(j-i)//2
    if check(k,mid,t):
        ans = mid
        j = mid-1
    else:
        i = mid+1

print(ans)


