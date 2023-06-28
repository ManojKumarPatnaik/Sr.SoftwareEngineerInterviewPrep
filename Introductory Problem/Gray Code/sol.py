n = int(input())

def gray(n):
    if n == 1:
        return ["0","1"]
    sub = gray(n-1)
    ans = []
    for i in sub:
        ans.append("0"+i)
    for i in sub[::-1]:
        ans.append('1'+i)
    return ans

print("\n".join(gray(n)))