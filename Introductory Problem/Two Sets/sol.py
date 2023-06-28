n = int(input())

sum = n*(n+1)//2
if sum%2 == 1:
    print('NO')
else:
    a = []
    b = []
    sack = sum//2
    for i in range(n,0,-1):
        if i<=sack:
            a.append(i)
            sack -= i
        else:
            b.append(i)
    print("YES")
    print(len(a))
    print(*a)
    print(len(b))
    print(*b)