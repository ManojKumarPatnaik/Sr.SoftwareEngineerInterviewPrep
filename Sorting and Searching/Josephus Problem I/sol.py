from collections import deque
n = int(input())
 
q = deque([i for i in range(1,n+1)])
 
while len(q) >0:
    length = len(q)
    for i in range(length):
        if i%2 == 0:
            q.append(q.popleft())
        else:
            print(q.popleft(),end=" ")

    if(length%2 == 1):
        print(q.popleft(),end=" ")