n = int(input())

timeline = [0]*(2*n)
for i in range(n):
    a,b = map(int,input().split())
    timeline[2*i],timeline[2*i+1] = 2*a,2*b+1

timeline.sort()

people = 0
ans = 0

for i in range(2*n):
    if timeline[i]%2 == 0: #one customer enters now
        people+=1
        ans = max(ans,people)
    else: #one customer leaves now
        people-=1

print(ans)