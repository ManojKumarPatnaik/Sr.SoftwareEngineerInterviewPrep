t = int(input())

while t>0:
    t-=1
    x,y = map(int,input().split())
     
    sq = max(x,y)
    if sq%2 == 0:
        print((sq-1)**2 + x + (sq-y))
    else:
        print(sq**2 - (x+ (sq-y)) + 1)

