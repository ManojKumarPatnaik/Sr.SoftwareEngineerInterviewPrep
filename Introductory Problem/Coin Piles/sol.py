t = int(input())
while t>0:
    t-=1
    a,b = map(int,input().split())
    if (a+b)%3 == 0 and a<=b*2 and b<=a*2:
        print("YES")
    else:
        print("NO")