from bisect import bisect_left
 
 
def fun(v,n):
    if len(v) == 0:
        return 0
 
    tail = [0]*(n+1)
    length = 1  
 
    tail[0] = v[0]
 
    for i in range(1, len(v)):
        if v[i] > tail[length-1]:
            tail[length] = v[i]
            length += 1
        else:
            tail[bisect_left(tail, v[i], 0, length-1)] = v[i]
    return length
 
n = int(input())
x = list(map(int,input().split()))
print(fun(x,n))
 