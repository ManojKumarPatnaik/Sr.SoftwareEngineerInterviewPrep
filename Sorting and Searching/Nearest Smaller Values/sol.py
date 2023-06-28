from collections import deque
n = int(input())

x = list(map(int,input().split()))

s = deque()
s.append(0)

for i in range(n):
    while len(s)>0 and x[s[-1]] >= x[i]:
        s.pop()
    if len(s) == 0:
        print(0,end=" ")
    else:
        print(s[-1]+1,end=" ")
    s.append(i)



