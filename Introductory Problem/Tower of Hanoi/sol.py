n = int(input())

print(2**n - 1)

def toh(n,source,destination,aux):
    if n == 1:
        print(source,destination)
        return
    toh(n-1,source,aux,destination)
    print(source,destination)
    toh(n-1,aux,destination,source)

toh(n,1,3,2)
